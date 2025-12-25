#!/usr/bin/env python3
"""
Programmatic Cost Analysis Example

Demonstrates how to use the CFO scripts programmatically in your own Python code.
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class CostAnalysisResult:
    """Results from cost analysis."""
    total_cost: float
    by_provider: Dict[str, float]
    by_category: Dict[str, float]
    service_count: int
    recommendations: List[str]
    timestamp: str


class CFOAnalyzer:
    """Wrapper for CFO cost analysis scripts."""

    def __init__(self, project_root: Path = Path.cwd()):
        self.project_root = project_root
        self.scripts_dir = project_root / ".claude/skills/cfo/scripts"

    def analyze_codebase(self) -> CostAnalysisResult:
        """
        Analyze codebase for cloud service usage and costs.

        Returns:
            CostAnalysisResult with cost breakdown and recommendations
        """
        # Run analyze_costs.py script
        result = subprocess.run(
            [
                "python",
                str(self.scripts_dir / "analyze_costs.py"),
                "--project-root", str(self.project_root),
                "--format", "json",
                "--output", "/tmp/cfo-analysis.json"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        # Load results
        with open("/tmp/cfo-analysis.json") as f:
            data = json.load(f)

        return CostAnalysisResult(
            total_cost=data['total_estimated_cost'],
            by_provider=data['by_provider'],
            by_category=data['by_category'],
            service_count=len(data['services']),
            recommendations=data['recommendations'],
            timestamp=data['timestamp']
        )

    def parse_billing_data(
        self,
        billing_file: Path,
        provider: str = "aws"
    ) -> Dict:
        """
        Parse actual billing data from cloud provider.

        Args:
            billing_file: Path to billing export (CSV or JSON)
            provider: Cloud provider ('aws', 'gcp', or 'azure')

        Returns:
            Dictionary with billing analysis
        """
        result = subprocess.run(
            [
                "python",
                str(self.scripts_dir / "parse_bills.py"),
                "--file", str(billing_file),
                "--provider", provider,
                "--format", "json",
                "--output", "/tmp/billing-analysis.json"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        with open("/tmp/billing-analysis.json") as f:
            return json.load(f)

    def forecast_costs(
        self,
        base_cost: float,
        months: int = 6,
        growth_rate: float = 0.10
    ) -> Dict:
        """
        Generate cost forecast.

        Args:
            base_cost: Current monthly cost baseline
            months: Number of months to forecast
            growth_rate: Monthly growth rate (e.g., 0.10 for 10%)

        Returns:
            Dictionary with forecast data
        """
        result = subprocess.run(
            [
                "python",
                str(self.scripts_dir / "forecast.py"),
                "--base-cost", str(base_cost),
                "--months", str(months),
                "--growth-rate", str(growth_rate),
                "--format", "json",
                "--output", "/tmp/forecast.json"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        with open("/tmp/forecast.json") as f:
            return json.load(f)

    def get_cost_delta(
        self,
        before_dir: Path,
        after_dir: Path
    ) -> Dict:
        """
        Compare costs between two versions of the codebase.

        Args:
            before_dir: Path to baseline codebase
            after_dir: Path to modified codebase

        Returns:
            Dictionary with cost delta analysis
        """
        # Analyze before
        result_before = subprocess.run(
            [
                "python",
                str(self.scripts_dir / "analyze_costs.py"),
                "--project-root", str(before_dir),
                "--format", "json",
                "--output", "/tmp/before-costs.json"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        # Analyze after
        result_after = subprocess.run(
            [
                "python",
                str(self.scripts_dir / "analyze_costs.py"),
                "--project-root", str(after_dir),
                "--format", "json",
                "--output", "/tmp/after-costs.json"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        # Load and compare
        with open("/tmp/before-costs.json") as f:
            before = json.load(f)

        with open("/tmp/after-costs.json") as f:
            after = json.load(f)

        before_cost = before['total_estimated_cost']
        after_cost = after['total_estimated_cost']
        delta = after_cost - before_cost
        pct_change = (delta / before_cost * 100) if before_cost > 0 else 0

        # Find new/removed services
        before_services = {(s['provider'], s['service']) for s in before['services']}
        after_services = {(s['provider'], s['service']) for s in after['services']}

        new_services = after_services - before_services
        removed_services = before_services - after_services

        return {
            'before_cost': before_cost,
            'after_cost': after_cost,
            'delta': delta,
            'pct_change': pct_change,
            'new_services': [{'provider': p, 'service': s} for p, s in new_services],
            'removed_services': [{'provider': p, 'service': s} for p, s in removed_services]
        }


# Example Usage
def main():
    """Example usage of programmatic CFO analysis."""

    analyzer = CFOAnalyzer()

    print("=" * 80)
    print("CFO Programmatic Analysis Example")
    print("=" * 80)

    # Example 1: Analyze current codebase
    print("\n1. Analyzing codebase for cloud costs...")
    try:
        result = analyzer.analyze_codebase()
        print(f"   Total Estimated Cost: ${result.total_cost:.2f}/month")
        print(f"   Services Found: {result.service_count}")
        print(f"   Providers: {', '.join(result.by_provider.keys())}")

        if result.recommendations:
            print(f"\n   Top Recommendation:")
            print(f"   - {result.recommendations[0]}")

    except subprocess.CalledProcessError as e:
        print(f"   Error: {e}")

    # Example 2: Parse billing data (if available)
    print("\n2. Parsing billing data...")
    sample_bill = Path(".claude/skills/cfo/examples/sample-data/aws-sample-bill.csv")

    if sample_bill.exists():
        try:
            billing = analyzer.parse_billing_data(sample_bill, provider="aws")
            print(f"   Actual Total Cost: ${billing['total_cost']:.2f}")
            print(f"   Billing Period: {billing['period_start']} to {billing['period_end']}")
            print(f"   Trend: {billing['trends']['trend']}")
        except subprocess.CalledProcessError as e:
            print(f"   Error: {e}")
    else:
        print("   (Sample billing data not found)")

    # Example 3: Generate forecast
    print("\n3. Generating 6-month cost forecast...")
    try:
        forecast = analyzer.forecast_costs(
            base_cost=250.00,  # Example: $250/month
            months=6,
            growth_rate=0.15   # 15% monthly growth
        )

        print(f"   Base Monthly Cost: ${forecast['base_monthly_cost']:.2f}")
        print(f"   6-Month Projection: ${forecast['total_projected']:.2f}")
        print(f"   Growth Rate: {forecast['growth_rate'] * 100:.1f}%/month")

        # Show first and last month
        first_month = forecast['forecast_periods'][0]
        last_month = forecast['forecast_periods'][-1]

        print(f"\n   {first_month['month']}: ${first_month['projected_cost']:.2f}")
        print(f"   {last_month['month']}: ${last_month['projected_cost']:.2f}")

    except subprocess.CalledProcessError as e:
        print(f"   Error: {e}")

    # Example 4: Alert on high costs
    print("\n4. Cost threshold check...")
    try:
        result = analyzer.analyze_codebase()
        threshold = 1000.00  # Alert if > $1000/month

        if result.total_cost > threshold:
            print(f"   ⚠️  WARNING: Costs (${result.total_cost:.2f}) exceed threshold (${threshold:.2f})")
        else:
            print(f"   ✅ Costs (${result.total_cost:.2f}) within threshold (${threshold:.2f})")

    except subprocess.CalledProcessError as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 80)
    print("Analysis complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
