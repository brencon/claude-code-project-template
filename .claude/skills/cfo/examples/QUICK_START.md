# CFO Skill - Quick Start Guide

> Get started with cloud cost analysis in 5 minutes.

---

## Step 1: Choose Your Scenario

Pick the scenario that best matches your situation:

### 🆕 New Project (Planning Stage)
**Goal**: Estimate costs before building

**Start here**: `scenarios/01-startup-mvp.md`

**Next steps**:
1. Read the scenario to understand typical costs
2. Modify for your specific stack
3. Run cost analysis as you add cloud services

---

### 📈 Growing Project (Have Some Infrastructure)
**Goal**: Understand current costs and optimize

**Start here**: Run cost analysis on your codebase

```bash
# Analyze your project
python .claude/skills/cfo/scripts/analyze_costs.py --project-root /path/to/your/project

# Or use slash command
/cfo analyze our cloud costs
```

**Next steps**:
1. Review the cost breakdown
2. Implement quick win optimizations
3. Set up cost monitoring (see Step 4)

---

### 🏢 Mature Project (Need to Cut Costs)
**Goal**: Find savings opportunities

**Start here**: `scenarios/02-ecommerce-growth.md` or `scenarios/03-enterprise-platform.md`

**Next steps**:
1. Get actual billing data from cloud provider
2. Parse and analyze: `python scripts/parse_bills.py --file billing.csv`
3. Implement optimization roadmap

---

## Step 2: Analyze Your Costs

### Option A: Code Analysis (Estimates)

```bash
# From project root
python .claude/skills/cfo/scripts/analyze_costs.py \
  --project-root . \
  --output cost-report.md
```

**What you get**:
- Estimated monthly costs by service
- Breakdown by provider and category
- Optimization recommendations

**Accuracy**: ±30% (estimates from code patterns)

---

### Option B: Billing Data (Actual Costs)

```bash
# AWS
python .claude/skills/cfo/scripts/parse_bills.py \
  --file aws-billing-june.csv \
  --provider aws \
  --output billing-analysis.md

# GCP
python .claude/skills/cfo/scripts/parse_bills.py \
  --file gcp-billing-june.json \
  --provider gcp \
  --output billing-analysis.md
```

**What you get**:
- Actual costs by service and region
- Cost trends and anomalies
- Top resource breakdown
- Peak usage days

**Accuracy**: 100% (actual billing data)

---

### Option C: Interactive (Slash Command)

```
/cfo
```

**Best for**: Quick analysis without leaving Claude Code

---

## Step 3: Generate a Forecast

```bash
# 6-month forecast with 10% growth
python .claude/skills/cfo/scripts/forecast.py \
  --base-cost 5000 \
  --months 6 \
  --growth-rate 0.10 \
  --output forecast.md
```

**Customize with**:
- `--historical '[4800, 4950, 5000, 5200]'` - Auto-estimate growth from data
- `--seasonal '{"12": 1.3, "1": 0.8}'` - Account for seasonal peaks

---

## Step 4: Set Up Monitoring

### A. Git Pre-Commit Hook (Recommended)

Warn developers when code changes increase costs:

```bash
# Install hook
ln -s ../../.claude/skills/cfo/scripts/pre-commit-cost-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**What it does**:
- Runs on every commit
- Compares against baseline
- Warns if costs increase >10%
- Blocks if costs increase >50%

**Customize thresholds**: Edit script variables `WARN_THRESHOLD` and `BLOCK_THRESHOLD`

---

### B. CI/CD Integration

**GitHub Actions**:
```bash
# Copy workflow file
cp .claude/skills/cfo/examples/integrations/github-actions-cost-check.yml \
   .github/workflows/cost-check.yml

# Commit and push
git add .github/workflows/cost-check.yml
git commit -m "Add cost analysis to CI"
git push
```

**What it does**:
- Runs on every PR
- Posts cost impact comment
- Fails if costs increase >50%
- Uploads cost reports as artifacts

---

### C. Programmatic (Python)

See `examples/integrations/programmatic_analysis.py` for:
- Custom cost thresholds
- Scheduled analysis
- Slack/email notifications
- Integration with monitoring tools

---

## Step 5: Take Action

### Quick Wins (1 hour, 10-30% savings)

From your cost analysis report, look for:

1. **Delete unused resources**
   - Orphaned volumes, snapshots
   - Forgotten dev instances
   - Old backups

2. **Downgrade over-provisioned**
   - Databases using <30% capacity
   - VMs with <20% CPU
   - Cache instances barely used

3. **Auto-shutdown dev/test**
   - Stop instances nights & weekends
   - Save 70% of dev costs

4. **Storage lifecycle policies**
   - Move old data to cheaper tiers
   - Archive logs after 90 days

---

### Strategic (1 week, 20-40% savings)

1. **Purchase Reserved Instances**
   - For workloads running 24/7
   - 30-70% discount
   - Payback: 12-36 months

2. **Implement auto-scaling**
   - Scale down during low traffic
   - Use Spot/Preemptible for batch jobs

3. **CDN/caching**
   - Reduce origin server load
   - Lower data transfer costs

---

### Architectural (1+ months, 30-50% savings)

1. **Serverless migration**
   - Pay only for actual usage
   - No idle capacity costs

2. **Database optimization**
   - Query tuning
   - Read replicas instead of larger primary
   - Sharding for scale

3. **Multi-region strategy**
   - Data locality reduces transfer
   - Regional pricing differences

---

## Common Workflows

### Weekly Cost Check
```bash
# Get current cost
python scripts/analyze_costs.py --project-root . | grep "Total Estimated"

# Compare to baseline
# If > 10% increase, investigate
```

---

### Monthly Billing Review
```bash
# Download billing CSV from cloud provider
# Parse and analyze
python scripts/parse_bills.py --file billing-june.csv --provider aws

# Look for:
# - Unexpected spikes
# - New high-cost resources
# - Trends (growing or shrinking)
```

---

### Quarterly Financial Planning
```bash
# Generate 12-month forecast
python scripts/forecast.py \
  --base-cost $(current_cost) \
  --months 12 \
  --growth-rate 0.15

# Use for:
# - Budget planning
# - Fundraising projections
# - Board presentations
```

---

### Pre-Architecture Decision
```bash
# Before: Analyze current state
python scripts/analyze_costs.py --project-root . --output before.json

# Make changes (in branch)
# After: Analyze new state
python scripts/analyze_costs.py --project-root . --output after.json

# Compare
python << 'EOF'
import json
with open('before.json') as f: before = json.load(f)
with open('after.json') as f: after = json.load(f)

print(f"Cost change: ${before['total_estimated_cost']:.2f} → ${after['total_estimated_cost']:.2f}")
print(f"Delta: ${after['total_estimated_cost'] - before['total_estimated_cost']:.2f}")
EOF
```

---

## Troubleshooting

### "No services found"

**Causes**:
- No cloud SDKs in code yet (expected for new projects)
- Cloud setup in separate infrastructure repo
- Using managed platforms (Vercel, Heroku) without code patterns

**Solutions**:
- Check other repos for infrastructure code
- Manually input known costs
- Use scenario templates as guide

---

### "Costs seem too high/low"

**Check**:
- Region (prices vary by region)
- Instance types (estimate uses defaults)
- Usage patterns (script estimates moderate usage)

**Fix**:
- Customize `COST_ESTIMATES` in `analyze_costs.py`
- Use actual billing data for precision
- Add region-specific multipliers

---

### "Script fails on my codebase"

**Common issues**:
- File permissions: `chmod +x scripts/*.py`
- Python version: Need Python 3.7+
- Character encoding: Ensure UTF-8

**Debug**:
```bash
# Run with verbose output
python scripts/analyze_costs.py --project-root . --debug
```

---

## Next Steps

### Learn More

- **Scenarios**: Explore realistic cost profiles in `scenarios/`
- **Examples**: See detailed use cases in `EXAMPLES.md`
- **Integration**: Set up CI/CD in `integrations/`
- **FinOps**: Read best practices in `references/finops-framework.md`

### Take Action

1. ✅ Run initial analysis (Step 2)
2. ✅ Implement 1-2 quick wins (Step 5)
3. ✅ Set up monitoring (Step 4)
4. ✅ Schedule monthly reviews

### Get Help

- **Documentation**: `README.md` for comprehensive guide
- **Skill Instructions**: `.claude/skills/cfo/skill.md`
- **Sample Data**: Test with files in `sample-data/`

---

## Quick Reference Commands

```bash
# Analyze codebase
python scripts/analyze_costs.py --project-root .

# Parse AWS bill
python scripts/parse_bills.py --file bill.csv --provider aws

# Forecast 6 months
python scripts/forecast.py --base-cost 5000 --months 6

# Install git hook
ln -s ../../.claude/skills/cfo/scripts/pre-commit-cost-check.sh .git/hooks/pre-commit

# Use slash command
/cfo analyze our infrastructure costs
```

---

**Ready to optimize?** Start with Step 2 and analyze your current costs! 🚀
