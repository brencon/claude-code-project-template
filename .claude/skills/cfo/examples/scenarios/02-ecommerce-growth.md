# Scenario 2: Growing E-Commerce Platform

> Mid-stage e-commerce business scaling to handle Black Friday traffic.

---

## Project Profile

**Stage**: Growth (2 years in operation)
**Monthly Orders**: 15,000 orders
**Daily Traffic**: 50K unique visitors
**Peak Traffic**: 200K visitors/day (holiday season)
**Team Size**: 12 engineers, 3 ops
**Monthly Revenue**: $450,000 (GMV)
**Take Rate**: 8% ($36,000/month revenue)

---

## Infrastructure Setup

### Hosting & Compute

**AWS EC2** (Web servers):
- 5× m5.large instances (production)
- 2× t3.medium instances (staging)
- Auto-scaling group (scale to 20 during peaks)
- **Cost**: $510/month base + $850/month peak capacity

**AWS Lambda** (Background jobs):
- Order processing, email notifications
- 5M invocations/month
- **Cost**: $85/month

### Database & Caching

**AWS RDS PostgreSQL**:
- db.r5.xlarge (4 vCPU, 32 GB RAM)
- Multi-AZ for high availability
- 500 GB storage
- **Cost**: $580/month

**AWS ElastiCache Redis**:
- cache.r5.large (2 shards for sessions + product catalog)
- **Cost**: $292/month

### Storage & CDN

**AWS S3**:
- Product images: 2 TB
- Order documents: 200 GB
- Backups: 500 GB
- **Cost**: $62/month storage

**CloudFront CDN**:
- 5 TB data transfer/month
- 50M requests/month
- **Cost**: $425/month

### Search & Analytics

**Elasticsearch** (AWS OpenSearch):
- 3× r5.large.search instances
- Product search + analytics
- **Cost**: $630/month

**AWS Redshift** (Data warehouse):
- dc2.large (2 nodes)
- Business intelligence queries
- **Cost**: $360/month

### Messaging & Queues

**AWS SQS** (Order processing queue):
- 20M requests/month
- **Cost**: $8/month

**AWS SNS** (Notifications):
- 5M publishes/month
- **Cost**: $2.50/month

### Payment Processing

**Stripe**:
- 15,000 transactions/month
- Average order: $30
- **Cost**: 2.9% + $0.30 = ~$13,500/month
- *Note: This is COGS, not infrastructure*

### Monitoring & Security

**Datadog** (Monitoring):
- 15 hosts, 500 GB logs/month
- **Cost**: $450/month

**AWS WAF** (DDoS protection):
- 10M requests/month
- **Cost**: $85/month

**PagerDuty** (On-call):
- Business plan for 15 users
- **Cost**: $396/month

### Email & SMS

**SendGrid** (Transactional):
- 500K emails/month
- **Cost**: $89.95/month

**Twilio** (SMS notifications):
- 50K SMS/month (order updates)
- **Cost**: $400/month

---

## Cost Breakdown

| Category | Services | Monthly Cost |
|----------|----------|--------------|
| **Compute** | EC2 (base) + Lambda | $595.00 |
| **Peak Capacity** | EC2 auto-scale | $850.00 |
| **Database** | RDS PostgreSQL | $580.00 |
| **Caching** | ElastiCache Redis | $292.00 |
| **Storage** | S3 | $62.00 |
| **CDN** | CloudFront | $425.00 |
| **Search** | OpenSearch | $630.00 |
| **Data Warehouse** | Redshift | $360.00 |
| **Messaging** | SQS + SNS | $10.50 |
| **Monitoring** | Datadog + PagerDuty | $846.00 |
| **Security** | AWS WAF | $85.00 |
| **Email** | SendGrid | $89.95 |
| **SMS** | Twilio | $400.00 |
| **TOTAL (Base)** | | **$5,225.45** |
| **TOTAL (Peak Months)** | | **$6,075.45** |

**Annual Cost**: ~$66,000 (averaging peak months)

*Note: Excludes Stripe payment processing fees ($13,500/mo) as those are cost of goods sold, not infrastructure.*

---

## CFO Analysis Report

### Executive Summary

**Monthly Infrastructure Cost**: $5,225 (base) / $6,075 (peak)
**Cost per Order**: $0.35 - $0.40
**Monthly Revenue**: $36,000
**Infrastructure as % of Revenue**: 14.5% - 16.9%
**Gross Margin** (excl. COGS): ~83%

### Financial Health: 🟡 Fair

**Strengths**:
- Revenue comfortably covers infrastructure (6.9x coverage)
- Auto-scaling handles peak traffic
- High availability architecture (Multi-AZ, redundancy)
- Comprehensive monitoring and security

**Concerns**:
- 🔴 **Peak capacity costs**: $850/month for 2-3 months/year (Black Friday, holidays)
- ⚠️ **Monitoring overhead**: $846/month (16% of infrastructure budget)
- ⚠️ **No reserved capacity**: Paying 100% on-demand rates
- ⚠️ **Redshift underutilized**: Running 24/7 for batch queries

---

## Cost Optimization Opportunities

### Quick Wins (Save $950/month - 18%)

1. **Purchase EC2 Reserved Instances**
   - **Current**: 5× m5.large on-demand ($510/month)
   - **Action**: 1-year standard RI (40% discount)
   - **New cost**: $306/month
   - **Savings**: $204/month

2. **RDS Reserved Instance**
   - **Current**: db.r5.xlarge on-demand ($580/month)
   - **Action**: 1-year standard RI (40% discount)
   - **New cost**: $348/month
   - **Savings**: $232/month

3. **ElastiCache Reserved Nodes**
   - **Current**: cache.r5.large on-demand ($292/month)
   - **Action**: 1-year RI (35% discount)
   - **New cost**: $190/month
   - **Savings**: $102/month

4. **S3 Intelligent-Tiering**
   - **Current**: All S3 Standard ($62/month)
   - **Action**: Auto-tier old product images, archives
   - **Savings**: $18/month (30% of S3 costs)

5. **CloudFront Savings Bundle**
   - **Current**: Pay-as-you-go ($425/month)
   - **Action**: Commit to 10 TB/month (you use 5 TB)
   - **New cost**: $340/month
   - **Savings**: $85/month

6. **Optimize Datadog**
   - **Current**: 500 GB logs/month indexed
   - **Action**: Use log archives (90% cheaper for older logs)
   - **New cost**: $350/month
   - **Savings**: $100/month

7. **Pause/Schedule Redshift**
   - **Current**: Running 24/7 ($360/month)
   - **Action**: Auto-pause when not in use (run 8 hours/day)
   - **New cost**: $120/month
   - **Savings**: $240/month

**Total Quick Wins**: $981/month (19% reduction)
**New Monthly Base Cost**: $4,244

### Strategic Optimizations (Quarter 2-3)

8. **Spot Instances for Staging**
   - **Current**: 2× t3.medium on-demand
   - **Savings**: 70% cost reduction
   - **Impact**: $85/month

9. **Migrate to Aurora Serverless v2**
   - **Current**: RDS always running at peak capacity
   - **Future**: Aurora scales to demand
   - **Potential savings**: 20-40% ($70-140/month)
   - **Effort**: 2-3 weeks migration

10. **CloudFront to S3 direct for backoffice**
    - **Action**: Serve admin dashboard from S3 (not CDN)
    - **Savings**: Reduce CloudFront by 10% (~$40/month)

11. **Consolidate email providers**
    - **Current**: SendGrid for transactional
    - **Opportunity**: Bundle with AWS SES
    - **New cost**: $40/month (vs $89.95)
    - **Savings**: $50/month

### Architectural Changes (6-12 months)

12. **Kubernetes on EKS**
    - **Current**: Individual EC2 instances
    - **Future**: Container orchestration with better bin packing
    - **Benefit**: 30% better resource utilization
    - **Savings**: $200-300/month

13. **Move to Graviton instances** (ARM)
    - **Benefit**: 20% better price-performance
    - **Savings**: $150-200/month
    - **Effort**: Test application compatibility

14. **Multi-region caching strategy**
    - Cache product catalog at edge (CloudFront Functions)
    - Reduce origin requests by 40%
    - **Savings**: $100-150/month

---

## Peak Traffic Strategy

### Current Approach: Over-Provision

**Problem**: Paying for peak capacity year-round or scrambling during peaks.

**Current peak handling**:
- Manual scale-up 1 week before Black Friday
- Costs spike from $5,225 to $6,075 (+16%)
- Runs for 8-12 weeks (Q4)
- **Extra cost**: $850 × 3 months = $2,550/year

### Optimized Approach: Auto-Scale + Reserved Base

**New strategy**:
1. **Base capacity**: 5 RI instances (always running)
2. **Auto-scale**: Spot instances for burst (90% cheaper)
3. **Lambda**: Handle more background tasks
4. **CloudFront**: Aggressive caching during peak

**Peak month costs with optimization**:
- Base (RI): $4,244
- Peak burst (Spot): $200/month (vs $850 on-demand)
- **Total**: $4,444/month
- **Savings during peak**: $631/month

**Annual peak savings**: $631 × 3 = $1,893

---

## Revenue Strategy

### Current Model
- **Revenue**: 8% take rate on GMV
- **GMV**: $450K/month
- **Net revenue**: $36K/month

**Infrastructure**: $5,225/month (14.5% of revenue)

### Optimization Opportunities

**Option 1: Increase Take Rate**
- **Current**: 8%
- **Industry benchmark**: 10-15%
- **Opportunity**: Increase to 10% (+$9K/month revenue)
- **Justification**: Platform improvements (search, analytics, faster checkout)

**Option 2: Introduce Premium Seller Tiers**
- **Free**: 8% take rate (current)
- **Premium**: 6% take rate + $199/month subscription
  - Featured listings
  - Priority support
  - Advanced analytics
- **Target**: 50 sellers × $199 = $9,950/month

**Option 3: Value-Added Services**
- **Fulfillment Services**: $2-5 per order handled
- **Marketing Tools**: $99-499/month
- **Data/Analytics**: $299/month
- **Potential**: $5-15K/month additional revenue

### Combined Revenue Projection

**Current**: $36,000/month

**With optimizations**:
- Take rate increase: +$9,000/month
- Premium tiers: +$10,000/month
- Value-added: +$8,000/month
- **New total**: $63,000/month (+75%)

**Infrastructure cost**: $4,244/month (optimized)
**Infrastructure as % of revenue**: 6.7% (improved from 14.5%)

---

## Unit Economics

### Per Order
- **Revenue per order**: $36,000 ÷ 15,000 = $2.40
- **Infrastructure cost per order**: $5,225 ÷ 15,000 = $0.35
- **Margin per order**: $2.05 (85%)

### Per Customer (Annual)
- **Average customer**: 12 orders/year
- **Revenue per customer**: $28.80/year
- **Infrastructure cost**: $4.20/year
- **CAC**: $45 (paid marketing)
- **LTV**: $144 (5-year avg, 60 orders)
- **LTV:CAC**: 3.2:1 (good)

### Profitability Thresholds
- **Break-even**: 2,177 orders/month
- **Current**: 15,000 orders/month (6.9x break-even)
- **Margin**: 85% (excellent)

---

## Forecasts

### 12-Month Cost Projection

| Month | Orders | Base Cost | Peak Add | Total | Revenue |
|-------|--------|-----------|----------|-------|---------|
| Jan | 12,000 | $4,244 | $0 | $4,244 | $28,800 |
| Feb | 13,000 | $4,244 | $0 | $4,244 | $31,200 |
| Mar | 14,000 | $4,244 | $0 | $4,244 | $33,600 |
| Apr | 15,000 | $4,244 | $0 | $4,244 | $36,000 |
| May | 16,000 | $4,244 | $0 | $4,244 | $38,400 |
| Jun | 17,000 | $4,244 | $0 | $4,244 | $40,800 |
| Jul | 18,000 | $4,244 | $0 | $4,244 | $43,200 |
| Aug | 19,000 | $4,244 | $0 | $4,244 | $45,600 |
| Sep | 20,000 | $4,244 | $0 | $4,244 | $48,000 |
| Oct | 25,000 | $4,244 | $200 | $4,444 | $60,000 |
| Nov | 35,000 | $4,244 | $200 | $4,444 | $84,000 |
| Dec | 30,000 | $4,244 | $200 | $4,444 | $72,000 |

**Annual Infrastructure Cost**: $51,524 (with optimizations)
**Annual Revenue**: $561,600
**Infrastructure as % of Revenue**: 9.2%

**Without optimizations**: $64,804 annually
**Savings**: $13,280/year (20%)

---

## Competitive Benchmarking

### E-Commerce Infrastructure Costs

| Metric | This Platform | Industry Avg | Grade |
|--------|---------------|--------------|-------|
| Cost per order | $0.35 | $0.40-0.80 | ✅ Excellent |
| Infrastructure % of revenue | 14.5% → 6.7% | 8-15% | ✅ Good → Excellent |
| Uptime | 99.9% | 99.9% | ✅ On par |
| Peak capacity handling | Manual → Auto | Auto-scale | 🟡 → ✅ |
| Reserved capacity | 0% → 60% | 50-70% | 🔴 → ✅ |

---

## Recommendations

### Immediate (Week 1)

1. ✅ **Purchase Reserved Instances**
   - 5× EC2 m5.large (1-year RI)
   - 1× RDS db.r5.xlarge (1-year RI)
   - 1× ElastiCache cache.r5.large (1-year RI)
   - **Savings**: $538/month
   - **Upfront cost**: $15,000 (payback: 28 months, but RI is 12 months)

2. ✅ **Implement S3 Lifecycle Policies**
   - Auto-tier to IA after 90 days
   - Archive to Glacier after 365 days
   - **Savings**: $18/month

3. ✅ **Configure Redshift Auto-Pause**
   - Pause after 1 hour idle
   - Schedule wake for batch jobs
   - **Savings**: $240/month

### Month 2

4. 📊 **Audit Datadog usage**
   - Archive old logs
   - Reduce retention to 30 days
   - **Savings**: $100/month

5. 🎯 **Set up Spot Fleet for staging**
   - Move 2× staging instances to Spot
   - **Savings**: $85/month

6. 💰 **Launch Premium Seller Program**
   - Target 10 beta sellers
   - **Revenue**: +$2,000/month

### Quarter 2

7. 🚀 **Migrate to Aurora Serverless**
   - Better cost scaling
   - Testing: 2 weeks, Migration: 1 week
   - **Savings**: $100-200/month

8. 📧 **Consolidate to AWS SES**
   - Replace SendGrid
   - **Savings**: $50/month

9. 🌍 **Optimize CloudFront**
   - Savings bundle commitment
   - **Savings**: $85/month

---

## Risk Assessment

### Infrastructure Risks

**High Priority**:
- 🔴 **Single database** (RDS): Needs read replicas for scaling
- 🔴 **No disaster recovery**: Need cross-region backups
- 🟡 **Monitoring costs**: Growing faster than revenue

**Medium Priority**:
- 🟡 **Elasticsearch costs**: Will increase with catalog growth
- 🟡 **Peak capacity**: Need better auto-scaling strategy

**Low Priority**:
- 🟢 **S3 costs**: Well-optimized
- 🟢 **Lambda**: Efficient, no concerns

### Financial Risks

**Revenue Risk**:
- Dependency on GMV growth
- Take rate compression (competitive pressure)
- **Mitigation**: Diversify revenue (premium tiers, services)

**Cost Risk**:
- Traffic spike beyond auto-scaling capacity
- AWS price increases
- **Mitigation**: Multi-cloud strategy, reserved capacity

---

## Key Takeaways

### Strengths
- ✅ Strong unit economics ($0.35 cost per $2.40 revenue)
- ✅ Scalable architecture (auto-scaling, serverless)
- ✅ Healthy margins (85%)

### Weaknesses
- ⚠️ Zero reserved capacity (leaving 30-40% savings on table)
- ⚠️ Monitoring overhead high (16% of budget)
- ⚠️ Manual peak capacity management

### Priority Actions
1. **High ROI**: Purchase RIs (save $538/month, ROI in 28 months)
2. **Quick wins**: S3 lifecycle, Redshift pause (save $258/month)
3. **Revenue growth**: Premium seller program (+$10K/month potential)

---

## Appendix: Detailed Cost Calculations

### EC2 Reserved Instance Analysis

**Current (On-Demand)**:
- 5× m5.large × 730 hours × $0.096/hr = $350.40/month
- With auto-scaling overhead: $510/month

**1-Year RI (All Upfront)**:
- 5× m5.large RI: $2,010/year = $167.50/month
- Auto-scaling (on-demand): $160/month
- **Total**: $327.50/month
- **Savings**: $182.50/month (36%)

**3-Year RI (All Upfront)**:
- 5× m5.large RI: $4,380/3 years = $121.67/month
- Auto-scaling: $160/month
- **Total**: $281.67/month
- **Savings**: $228.33/month (45%)

**Recommendation**: 1-year RI for flexibility

---

**End of Scenario Analysis**
