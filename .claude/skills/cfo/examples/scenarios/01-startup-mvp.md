# Scenario 1: Startup MVP (Small SaaS)

> Early-stage startup building a B2B SaaS product with limited traffic.

---

## Project Profile

**Stage**: Pre-product/market fit
**Users**: 50 beta customers
**Traffic**: ~10K requests/day
**Team Size**: 3 engineers
**Monthly Revenue**: $500 (early beta customers)

---

## Infrastructure Setup

### Hosting & Compute
- **Vercel** (Next.js frontend)
  - Pro plan for team features
  - **Cost**: $20/month

- **AWS Lambda** (Serverless API)
  - 300K invocations/month
  - 128 MB memory, 200ms avg duration
  - **Cost**: $3.50/month

### Database
- **PostgreSQL on Heroku**
  - Standard-0 plan (64 GB storage)
  - **Cost**: $50/month

- **Redis on Upstash** (Caching)
  - Pay-as-you-go tier
  - **Cost**: $8/month

### Storage
- **AWS S3** (User uploads)
  - 5 GB stored
  - 10 GB transfer/month
  - **Cost**: $2.50/month

### Monitoring & Observability
- **Sentry** (Error tracking)
  - Team plan
  - **Cost**: $26/month

- **LogRocket** (Session replay)
  - Starter plan
  - **Cost**: $99/month

### Email & Communication
- **SendGrid** (Transactional email)
  - 40K emails/month (free tier)
  - **Cost**: $0/month

### Authentication
- **Auth0** (Free tier)
  - Up to 7,000 MAUs
  - **Cost**: $0/month

---

## Cost Breakdown

| Category | Services | Monthly Cost |
|----------|----------|--------------|
| **Hosting** | Vercel | $20.00 |
| **Compute** | AWS Lambda | $3.50 |
| **Database** | Heroku Postgres + Upstash Redis | $58.00 |
| **Storage** | AWS S3 | $2.50 |
| **Monitoring** | Sentry + LogRocket | $125.00 |
| **Email** | SendGrid | $0.00 |
| **Auth** | Auth0 | $0.00 |
| **TOTAL** | | **$209.00** |

---

## CFO Analysis Report

### Executive Summary

**Monthly Infrastructure Cost**: $209/month
**Cost per Customer**: $4.18/customer
**Current Revenue**: $500/month
**Burn Rate**: Net positive ($291/month profit from customers)
**Margin**: 58% (good for early stage)

### Financial Health: 🟢 Good

**Strengths**:
- Revenue covers infrastructure costs
- Efficient serverless architecture
- Good use of free tiers (Auth0, SendGrid)
- Low fixed costs enable experimentation

**Concerns**:
- ⚠️ LogRocket ($99/mo) is 47% of total costs for only 50 users
- ⚠️ No scaling discounts in place yet
- ⚠️ Monitoring costs may grow faster than revenue

---

## Cost Optimization Opportunities

### Quick Wins (Save $105/month - 50%)

1. **Replace LogRocket with lighter alternative**
   - **Current**: LogRocket at $99/month
   - **Alternative**: PostHog self-hosted or Hotjar Starter ($39/mo)
   - **Savings**: $60-99/month
   - **Trade-off**: Fewer features, but adequate for MVP stage

2. **Optimize Sentry usage**
   - **Current**: Team plan at $26/month
   - **Action**: Use error sampling (50% instead of 100%)
   - **Savings**: Switch to Developer plan at $0/month
   - **Impact**: Still captures critical errors

3. **Right-size database**
   - **Current**: Heroku Standard-0 at $50/month
   - **Analysis**: Currently using ~8 GB of 64 GB (12.5% utilized)
   - **Alternative**: Mini plan at $5/month or Supabase free tier
   - **Savings**: $45/month
   - **Risk**: Low (plenty of headroom)

**Total Quick Wins**: $105/month (50% reduction)
**New Monthly Cost**: $104/month
**New Margin**: 79%

### Strategic Optimizations (Month 3-6)

4. **Consolidate on AWS**
   - **Current**: Vercel ($20) + AWS Lambda + S3
   - **Future**: AWS Amplify Hosting ($15) + Lambda + S3
   - **Savings**: $5/month + unified billing
   - **Effort**: 1 week migration

5. **Implement CDN caching**
   - **Current**: Direct S3 access
   - **Future**: CloudFront (AWS free tier covers 1 TB/month)
   - **Savings**: Reduce S3 data transfer costs
   - **Benefit**: Faster performance

### Long-Term (When scaling to 500+ users)

6. **Reserved Capacity**
   - Purchase RDS Reserved Instance (40% savings)
   - Commit to Lambda Provisioned Concurrency
   - Estimated savings: $100+/month at scale

---

## Revenue Strategy

### Current Pricing
- **Beta pricing**: $10/user/month
- **Conversion rate**: 50 users × $10 = $500/month

### Recommended Pricing Model

**Freemium Tiers**:

| Tier | Price | Features | Target |
|------|-------|----------|--------|
| **Free** | $0 | 1 user, 1,000 API calls/mo | Individuals, testing |
| **Starter** | $29/mo | Up to 5 users, 50K calls/mo | Small teams |
| **Pro** | $99/mo | Up to 20 users, 500K calls/mo | Growing companies |
| **Enterprise** | Custom | Unlimited, SLA, support | Large orgs |

### Revenue Projections

**Conservative** (6 months):
- 500 free users (0% convert) = $0
- 50 Starter customers (80% of paid) = $1,450/month
- 10 Pro customers (20% of paid) = $990/month
- **Total**: $2,440/month

**Costs at this scale**: ~$350/month (with optimizations)
**Margin**: 86%
**Profitability**: ✅ Profitable

**Growth** (12 months):
- 2,000 free users
- 150 Starter = $4,350/month
- 40 Pro = $3,960/month
- 5 Enterprise ($500 avg) = $2,500/month
- **Total**: $10,810/month

**Costs at this scale**: ~$1,200/month
**Margin**: 89%
**Annual Run Rate**: ~$130K

---

## Forecasts

### 6-Month Cost Projection

| Month | Users | Infrastructure | Growth | Total |
|-------|-------|----------------|--------|-------|
| M1 | 50 | $209 | 0% | $209 |
| M2 | 75 | $220 | +5% | $220 |
| M3 | 120 | $245 | +11% | $245 |
| M4 | 180 | $280 | +14% | $280 |
| M5 | 280 | $325 | +16% | $325 |
| M6 | 400 | $385 | +18% | $385 |

**Total 6-month cost**: $1,664
**Average monthly**: $277

**With optimizations applied**:
**Total 6-month cost**: $950
**Savings**: $714 (43%)

---

## Recommendations

### Immediate Actions (This Week)

1. ✅ **Cancel or downgrade LogRocket**
   - Move to PostHog or reduce session capture
   - Save $60-99/month immediately

2. ✅ **Downgrade Heroku Postgres**
   - Mini plan sufficient for <200 users
   - Save $45/month

3. ✅ **Set up AWS budget alerts**
   - Alert at $50/month (current Lambda+S3 ~$6)
   - Prevent surprise overages

### Month 2-3

4. 📊 **Implement usage tracking**
   - Track API calls per customer
   - Identify power users (monetization opportunity)

5. 💰 **Launch pricing tiers**
   - Move beyond beta pricing
   - Target: 10 paid customers at $29-99/month

6. 🏷️ **Add cost allocation tags**
   - Tag AWS resources by environment (prod/staging/dev)
   - Enable better cost tracking

### Quarter 2

7. 🚀 **Plan for scale**
   - Implement auto-scaling
   - Move to Aurora Serverless (better economics at scale)
   - Consider reserved capacity

---

## Unit Economics

### Current
- **Cost per User**: $4.18/month
- **Revenue per User**: $10/month
- **Margin per User**: $5.82 (58%)
- **Customer LTV** (12 mo avg): $120
- **CAC** (organic): ~$0 (beta users)
- **LTV:CAC**: Infinite (organic acquisition)

### Target (Post-optimization)
- **Cost per User**: $2.08/month (optimized)
- **Revenue per User**: $30/month (new pricing)
- **Margin per User**: $27.92 (93%)
- **Customer LTV** (24 mo avg): $720
- **CAC** (paid): $150 (target)
- **LTV:CAC**: 4.8:1 (excellent)

---

## Competitive Benchmarking

### Industry Standards (B2B SaaS)

| Metric | This Project | Industry Avg | Grade |
|--------|--------------|--------------|-------|
| Infrastructure cost per user | $4.18 | $5-15 | ✅ Good |
| Gross margin | 58% | 70-85% | 🟡 Fair |
| Burn rate | Break-even | -$10-50K | ✅ Excellent |
| Cost of revenue | 42% | 15-30% | 🔴 High |

**Assessment**: Infrastructure costs are efficient, but monitoring overhead is high for this stage. After optimization, all metrics move to "Good" or "Excellent."

---

## Key Takeaways

### Strengths
- ✅ Revenue positive from day one
- ✅ Serverless architecture scales well
- ✅ Good use of free tiers
- ✅ Low customer acquisition cost

### Areas for Improvement
- ⚠️ Monitoring costs too high (47% of budget)
- ⚠️ Database over-provisioned (88% unused)
- ⚠️ No pricing tiers (leaving money on table)

### Action Plan Priority
1. **High Impact, Low Effort**: Downgrade database, reduce monitoring costs
2. **High Impact, Medium Effort**: Launch tiered pricing
3. **Medium Impact, Low Effort**: Set up cost alerts and tagging

---

## Appendix: Sample Invoice Breakdown

**Month 1 Actual Costs**:
```
Vercel Pro                    $20.00
AWS (Lambda + S3 + Data)      $ 6.15
Heroku Standard-0             $50.00
Upstash Redis                 $ 8.23
Sentry Team                   $26.00
LogRocket Starter             $99.00
SendGrid (Free)               $ 0.00
Auth0 (Free)                  $ 0.00
--------------------------------
Total                        $209.38
```

**Post-Optimization Target**:
```
Vercel Pro                    $20.00
AWS (Lambda + S3 + Data)      $ 6.15
Heroku Mini                   $ 5.00
Upstash Redis                 $ 8.23
Sentry (Free, sampled)        $ 0.00
PostHog Cloud Starter         $39.00
SendGrid (Free)               $ 0.00
Auth0 (Free)                  $ 0.00
--------------------------------
Total                        $78.38
Savings                      $131.00 (63%)
```

---

**End of Scenario Analysis**
