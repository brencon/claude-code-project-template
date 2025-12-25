# CFO Skill Examples

> Real-world scenarios, sample data, and integration examples for the CFO skill.

---

## 📂 What's Inside

### `/scenarios` - Realistic Project Profiles

Complete financial analyses for different project stages:

| Scenario | Monthly Cost | Description |
|----------|--------------|-------------|
| **01-startup-mvp.md** | $209 → $104 | Early-stage SaaS, 50 beta users, optimization roadmap |
| **02-ecommerce-growth.md** | $5,225 → $4,244 | Growing e-commerce, 15K orders/month, reserved instance strategy |
| **03-enterprise-platform.md** | $278,900 → $246,400 | Enterprise B2B platform, 500K users, multi-cloud FinOps |

**Use cases**:
- Benchmark your costs against similar projects
- Learn common optimization patterns
- Understand revenue strategies for each stage
- See realistic cost projections and forecasts

---

### `/sample-data` - Test Billing Data

Sample billing exports for testing scripts:

| File | Provider | Format | Contents |
|------|----------|--------|----------|
| **aws-sample-bill.csv** | AWS | CSV | 34 line items, $2,100 total |
| **gcp-sample-bill.json** | GCP | JSON | 10 line items, $566 total |

**Use cases**:
- Test billing parser without real data
- Learn billing export formats
- Validate script functionality
- Practice cost analysis workflows

**Try it**:
```bash
python scripts/parse_bills.py --file examples/sample-data/aws-sample-bill.csv --provider aws
```

---

### `/integrations` - CI/CD & Automation

Integration examples for production use:

| File | Type | Purpose |
|------|------|---------|
| **github-actions-cost-check.yml** | GitHub Actions | PR cost impact analysis |
| **programmatic_analysis.py** | Python API | Programmatic script usage |

**Use cases**:
- Automated cost checks on every PR
- Custom monitoring and alerting
- Integration with existing tools
- Scheduled cost analysis

---

### `QUICK_START.md` - 5-Minute Guide

Step-by-step walkthrough to get started:

1. Choose your scenario
2. Analyze your costs
3. Generate a forecast
4. Set up monitoring
5. Take action (quick wins → strategic → architectural)

**Perfect for**: First-time users who want to dive right in.

---

## 🚀 Quick Start Paths

### Path 1: Planning a New Project

**Goal**: Estimate costs before building

```bash
# 1. Read startup scenario
cat examples/scenarios/01-startup-mvp.md

# 2. Modify for your stack
# (edit the scenario or create your own)

# 3. Monitor as you build
/cfo analyze expected costs
```

**Time**: 15 minutes

---

### Path 2: Analyzing Existing Project

**Goal**: Understand current spending

```bash
# 1. Analyze codebase
python scripts/analyze_costs.py --project-root /path/to/project --output costs.md

# 2. Get actual billing data (optional but recommended)
# Download from AWS/GCP/Azure console

# 3. Parse billing
python scripts/parse_bills.py --file billing.csv --provider aws --output billing.md

# 4. Compare and optimize
# Look for mismatches between estimated and actual
```

**Time**: 30 minutes

---

### Path 3: Cutting Costs

**Goal**: Find and implement savings

```bash
# 1. Read optimization scenario matching your scale
cat examples/scenarios/02-ecommerce-growth.md  # or 03-enterprise-platform.md

# 2. Run your own analysis
/cfo find 30% cost reduction opportunities

# 3. Implement quick wins (from the report)
# - Delete unused resources
# - Rightsize over-provisioned
# - Implement lifecycle policies

# 4. Track savings over time
python scripts/forecast.py --base-cost <current> --months 6
```

**Time**: 1-2 hours (analysis), days-weeks (implementation)

---

### Path 4: Setting Up Automation

**Goal**: Continuous cost awareness

```bash
# 1. Install git hook
ln -s ../../.claude/skills/cfo/scripts/pre-commit-cost-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# 2. Add CI/CD workflow
cp examples/integrations/github-actions-cost-check.yml .github/workflows/

# 3. Configure thresholds
# Edit hook and workflow for your needs

# 4. Test
git commit -m "test cost check"  # Should see cost analysis
```

**Time**: 15 minutes

---

## 📊 Example Outputs

### Scenario Analysis Output

```markdown
# CFO Financial Analysis Report

**Monthly Infrastructure Cost**: $209.00
**Cost per Customer**: $4.18/customer
**Gross Margin**: 58%

## Quick Wins (Save $105/month - 50%)
1. Replace LogRocket → Save $60-99/month
2. Downgrade database → Save $45/month
...

## Revenue Strategy
**Recommended Pricing**: Freemium + Usage-based
- Free: 1K API calls
- Starter: $29/mo
- Pro: $99/mo
...
```

### Billing Analysis Output

```markdown
# Cloud Billing Analysis

**Total Cost**: $2,666.00
**Trend**: Increasing (+12%)

## By Service
- EC2: $745 (28%)
- RDS: $701 (26%)
- CloudFront: $288 (11%)
...

## Top Resources
1. db-cluster-apidb: $701/month
2. Production EC2 instances: $582/month
...
```

### Forecast Output

```markdown
# Cloud Cost Forecast

**6-Month Projection**: $32,500
**Growth Rate**: 10%/month

| Month | Projected | Confidence |
|-------|-----------|------------|
| Jan   | $5,000    | High       |
| Jun   | $8,053    | Medium     |
...
```

---

## 🎓 Learning Resources

### For Beginners

1. Start with `QUICK_START.md`
2. Read `scenarios/01-startup-mvp.md`
3. Try sample data: `python scripts/parse_bills.py --file examples/sample-data/aws-sample-bill.csv`

### For Intermediate Users

1. Compare your costs to scenarios
2. Set up git hook automation
3. Generate custom forecasts

### For Advanced Users

1. Customize scripts for your pricing
2. Build programmatic integrations
3. Implement full FinOps workflows

---

## 💡 Tips & Best Practices

### Analyzing Costs

✅ **Do**:
- Use actual billing data when available (100% accuracy)
- Run analysis monthly
- Track trends over time
- Compare against industry benchmarks (see scenarios)

❌ **Don't**:
- Rely solely on estimates (±30% variance)
- Ignore small costs (they add up)
- Optimize once and forget (costs drift)
- Focus only on costs (consider business value)

### Implementing Savings

✅ **Do**:
- Start with quick wins (low effort, high impact)
- Test changes in staging first
- Monitor impact of optimizations
- Celebrate wins with team

❌ **Don't**:
- Cut costs at expense of reliability
- Commit to long-term RIs without analysis
- Over-optimize development environments
- Ignore CAC and LTV when cutting costs

### Revenue Strategy

✅ **Do**:
- Price based on value, not cost
- Offer multiple tiers
- Track unit economics
- Test pricing changes with data

❌ **Don't**:
- Race to the bottom on price
- Underprice to compete
- Ignore customer willingness to pay
- Set pricing once and never change

---

## 🔧 Customization

### Add Your Own Scenario

1. Copy a template:
   ```bash
   cp scenarios/01-startup-mvp.md scenarios/my-project.md
   ```

2. Update:
   - Project profile (users, traffic, revenue)
   - Infrastructure setup (actual services)
   - Cost breakdown (real or estimated costs)
   - Optimization opportunities

3. Use as reference:
   ```
   /cfo compare my costs to scenarios/my-project.md
   ```

### Extend Sample Data

Add your sanitized billing data:

```bash
# AWS
# Export Cost and Usage Report from AWS Console
# Save to examples/sample-data/my-aws-bill.csv

# GCP
# Export billing to BigQuery or Cloud Storage
# Download and save as my-gcp-bill.json

# Test
python scripts/parse_bills.py --file examples/sample-data/my-aws-bill.csv
```

### Create Custom Integration

See `integrations/programmatic_analysis.py` as template:

```python
from cfo_analyzer import CFOAnalyzer

analyzer = CFOAnalyzer()
result = analyzer.analyze_codebase()

if result.total_cost > MY_THRESHOLD:
    send_slack_alert(f"Costs: ${result.total_cost}")
```

---

## 🆘 Troubleshooting

### Issue: "No services found in codebase"

**Solution**: This is normal for:
- New projects (no cloud services yet)
- Infrastructure defined elsewhere (separate repo)
- Fully managed platforms (no SDK in code)

**Action**: Use scenarios as reference or input costs manually

### Issue: "Costs don't match actual bill"

**Remember**: Code analysis gives estimates (±30%)

**Solution**: Use `parse_bills.py` with actual billing exports for accuracy

### Issue: "Script errors on my data"

**Check**:
- Python version (need 3.7+)
- File encoding (UTF-8)
- File format (AWS CSV vs GCP JSON)

**Debug**:
```bash
python scripts/parse_bills.py --file bill.csv --provider aws --debug
```

---

## 📚 Additional Documentation

- **Main README**: `../README.md`
- **Skill Instructions**: `../skill.md`
- **Scripts Guide**: `../scripts/README.md`
- **Hooks Setup**: `../HOOKS_SETUP.md`
- **Usage Examples**: `../EXAMPLES.md`
- **FinOps Framework**: `../references/finops-framework.md`

---

## 🎯 Next Steps

1. **Quick Start**: Read `QUICK_START.md` for 5-minute walkthrough
2. **Pick Scenario**: Find one matching your project stage
3. **Analyze Costs**: Run scripts on your project
4. **Take Action**: Implement quick win optimizations
5. **Automate**: Set up git hooks and CI/CD

---

**Questions?** See the main README or use `/cfo` for interactive help!
