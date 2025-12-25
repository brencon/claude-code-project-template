# Sample Billing Data

> Test data files for CFO skill billing analysis scripts.

---

## Available Sample Files

### AWS Cost and Usage Report
**File**: `aws-sample-bill.csv`

**Format**: CSV (AWS CUR standard format)

**Contents**:
- 34 line items across 2 days (June 1-2, 2024)
- Mix of production, staging, and development environments
- Services: EC2, RDS, Lambda, S3, DynamoDB, CloudFront, ElastiCache, CloudWatch, SNS, SQS, WAF, Route53, VPC, KMS, Secrets Manager
- Total cost: ~$2,100 for the period shown
- Includes cost allocation tags (Environment, Team, Project)

**Usage**:
```bash
python .claude/skills/cfo/scripts/parse_bills.py \
  --file .claude/skills/cfo/examples/sample-data/aws-sample-bill.csv \
  --provider aws \
  --format markdown
```

---

### GCP Billing Export
**File**: `gcp-sample-bill.json`

**Format**: JSON (GCP billing export format)

**Contents**:
- 10 line items for June 1, 2024
- Mix of production and development environments
- Services: Compute Engine, Cloud Storage, Cloud SQL, Cloud Functions, Pub/Sub, BigQuery, Cloud CDN, Firestore
- Total cost: ~$566 for the period shown
- Includes labels (environment, team, project)

**Usage**:
```bash
python .claude/skills/cfo/scripts/parse_bills.py \
  --file .claude/skills/cfo/examples/sample-data/gcp-sample-bill.json \
  --provider gcp \
  --format markdown
```

---

## Sample Data Characteristics

### Cost Breakdown (Combined)

| Provider | Total | % |
|----------|-------|---|
| AWS | $2,100 | 79% |
| GCP | $566 | 21% |
| **Total** | **$2,666** | 100% |

### By Category

| Category | Cost | % |
|----------|------|---|
| Compute | $815 | 31% |
| Database | $684 | 26% |
| Storage | $247 | 9% |
| CDN | $368 | 14% |
| Messaging | $10 | <1% |
| Analytics | $250 | 9% |
| Monitoring | $91 | 3% |
| Other | $201 | 8% |

### By Environment

| Environment | Cost | % |
|-------------|------|---|
| Production | $2,450 | 92% |
| Staging | $146 | 5.5% |
| Development | $70 | 2.5% |

---

## Testing Scenarios

### Scenario 1: Basic Cost Analysis

**Goal**: Parse billing data and generate cost breakdown

```bash
# AWS
python .claude/skills/cfo/scripts/parse_bills.py \
  --file .claude/skills/cfo/examples/sample-data/aws-sample-bill.csv \
  --provider aws

# GCP
python .claude/skills/cfo/scripts/parse_bills.py \
  --file .claude/skills/cfo/examples/sample-data/gcp-sample-bill.json \
  --provider gcp
```

**Expected Output**:
- Total cost summary
- Cost by service
- Cost by region
- Top resources by cost
- Daily cost trend

### Scenario 2: Cost Allocation

**Goal**: Analyze costs by tags/labels

**AWS tags available**:
- `Environment`: production, staging, development
- `Team`: backend, database, storage, cdn, messaging, monitoring, security, networking
- `Project`: api-service, assets, backups, order-processor, sessions, notifications, job-queue, dns, nat, encryption, secrets, dev-env

**GCP labels available**:
- `environment`: production, development
- `team`: backend, storage, database, compute, messaging, analytics, cdn
- `project`: api-service, assets, order-processor, events, data-warehouse, realtime-data, dev-env

**Analysis**:
```bash
# The scripts automatically group by tags/labels
python .claude/skills/cfo/scripts/parse_bills.py \
  --file .claude/skills/cfo/examples/sample-data/aws-sample-bill.csv \
  --provider aws \
  --format markdown
```

### Scenario 3: Optimization Opportunities

**Goal**: Identify cost savings

**Known opportunities in sample data**:

1. **EC2 Reserved Instances**
   - 4× m5.large instances running 24/7 in production
   - Current: $145.60 each = $582.40/month
   - With 1-year RI (40% discount): $349.44/month
   - **Savings**: $232.96/month

2. **RDS Reserved Instance**
   - db.r5.xlarge running 24/7
   - Current: $350.40/month
   - With 1-year RI (40% discount): $210.24/month
   - **Savings**: $140.16/month

3. **Development Environment Auto-Shutdown**
   - 3× dev instances (2 AWS + 1 GCP) running 24/7
   - If shutdown nights & weekends (save 70% of time)
   - Current: $59/month
   - Optimized: $17.70/month
   - **Savings**: $41.30/month

4. **S3 Lifecycle Policies**
   - Backups stored in S3 Standard ($98.50/month)
   - Move to Glacier after 30 days
   - **Savings**: ~$75/month (76% reduction on old backups)

**Total Potential Savings**: $489.42/month (23% reduction)

### Scenario 4: Multi-Cloud Cost Comparison

**Goal**: Compare AWS vs GCP costs for similar workloads

**Compute Comparison**:
- AWS m5.large: $145.60/month
- GCP e2-standard-4 (similar spec): $24.50/month (sample shows only partial costs)

**Database Comparison**:
- AWS RDS PostgreSQL (db.r5.xlarge): $350.40/month
- GCP Cloud SQL PostgreSQL (similar): $150/month

**Storage Comparison**:
- AWS S3 (2TB): $45.80/month
- GCP Cloud Storage (1TB): $20/month

### Scenario 5: Trend Analysis

**Goal**: Identify cost trends over time

**Note**: Sample data only includes 2 days, but shows pattern:

**Day 1 (June 1)**: $2,073
**Day 2 (June 2)**: $656 (partial data)

**For realistic trend analysis**, you'd need 30-90 days of data.

---

## Creating Your Own Test Data

### AWS CSV Format

Required columns:
```csv
lineItem/UsageStartDate,lineItem/ProductCode,product/region,lineItem/ResourceId,lineItem/UnblendedCost,lineItem/UsageAmount,lineItem/UsageType,resourceTags/user:Environment,resourceTags/user:Team,resourceTags/user:Project
```

**Tips**:
- Use ISO 8601 format for dates: `2024-06-01T00:00:00Z`
- `lineItem/UnblendedCost`: Actual cost in USD
- `lineItem/UsageAmount`: Units consumed
- Tags are optional but recommended

### GCP JSON Format

Required fields:
```json
{
  "usage_start_time": "2024-06-01T00:00:00Z",
  "service": {
    "description": "Service Name"
  },
  "cost": 100.00,
  "usage": {
    "amount": 730,
    "unit": "hour"
  },
  "location": {
    "region": "us-central1"
  },
  "labels": {
    "environment": "production"
  }
}
```

---

## Expected Outputs

### Cost Summary
```markdown
# Cloud Billing Analysis

**Period**: 2024-06-01 to 2024-06-02
**Total Cost**: $2,666.00
**Line Items**: 44

## Cost Trends
**Trend**: Insufficient data (need 7+ days)
**Average Daily Cost**: $1,333.00

## By Service
- AmazonEC2: $745 (28%)
- AmazonRDS: $701 (26%)
- CloudFront: $288 (11%)
- BigQuery: $250 (9%)
- ...
```

### Top Resources
```markdown
## Top 10 Resources by Cost
1. db-cluster-apidb (RDS): $701.00
2. i-0abc123def456 (EC2): $291.20
3. i-0abc123def457 (EC2): $291.20
4. CloudFront Distribution: $287.65
...
```

---

## Integration with CFO Skill

### Via Slash Command
```
/cfo analyze billing data at .claude/skills/cfo/examples/sample-data/aws-sample-bill.csv
```

### Programmatically
```python
from pathlib import Path
import subprocess

# Parse AWS bill
result = subprocess.run([
    "python",
    ".claude/skills/cfo/scripts/parse_bills.py",
    "--file", ".claude/skills/cfo/examples/sample-data/aws-sample-bill.csv",
    "--provider", "aws",
    "--format", "json",
    "--output", "aws-analysis.json"
], capture_output=True, text=True)

print(result.stdout)
```

---

## Limitations

### Sample Data Limitations

1. **Not Real Costs**: Synthetic data for testing only
2. **Limited Time Range**: Only 2 days (real analysis needs 30-90 days)
3. **Simplified**: Real billing data has 100+ columns
4. **No Credits/Discounts**: Sample doesn't include promotional credits, RIs, etc.

### For Production Use

**Always use actual billing exports**:
- AWS: Enable Cost and Usage Report
- GCP: Export to BigQuery or Cloud Storage
- Azure: Export to Storage Account

---

## Troubleshooting

### "Error parsing file"

**Check**:
- File encoding (should be UTF-8)
- CSV delimiter (should be comma)
- JSON validity (use `jq` or `python -m json.tool`)

### "No data found"

**Check**:
- File path is correct
- Provider flag matches file type (`--provider aws` for CSV, `--provider gcp` for JSON)

### "Unexpected columns"

**Note**: Real AWS CUR files have 200+ columns. The parser only uses key columns.

---

**Need more sample data?** See the scenario files in `../scenarios/` for realistic cost profiles:
- `01-startup-mvp.md`: ~$200/month infrastructure
- `02-ecommerce-growth.md`: ~$5,000/month infrastructure
- `03-enterprise-platform.md`: ~$278,000/month infrastructure
