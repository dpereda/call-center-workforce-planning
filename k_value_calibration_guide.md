# K-Value Calibration Guide
## Finding Your Optimal Square Root Staffing Multiplier

This guide shows you how to calibrate the **k-value** in the Square Root Staffing formula based on your historical performance data and service level targets.

---

## Understanding the K-Value

In the formula:
```
Required Agents = Traffic + k × √Traffic
```

The **k-value** determines how much buffer capacity you add beyond base staffing needs.

- **Higher k** = More agents = Better service level = Higher cost
- **Lower k** = Fewer agents = Lower service level = Lower cost

Your goal: Find the **minimum k** that consistently achieves your target service level.

---

## Method 1: Reverse Engineering from Historical Data

Use this when you have actual performance data showing agents staffed and service levels achieved.

### Step-by-Step Process

#### Step 1: Gather Historical Data

You need at least 2-4 weeks of interval-level data with:
- Date & Time Interval
- Calls Offered
- Average Handle Time (AHT)
- Agents Actually Staffed
- Service Level Achieved (% answered within target)
- Abandonment Rate

**Your current data has this!** (from `call_center_arrival_pattern.csv`)

#### Step 2: Calculate Traffic for Each Interval

```excel
Traffic = (Calls_Offered × AHT_Seconds) / Interval_Seconds
```

For 15-minute intervals:
```excel
= D2 * H2 / 900
```

#### Step 3: Reverse Calculate K-Value

Rearrange the formula to solve for k:

```
k = (Agents - Traffic) / √Traffic
```

**Excel Formula:**
```excel
= (Agents_Actually_Staffed - Traffic_Intensity) / SQRT(Traffic_Intensity)
```

#### Step 4: Create Calibration Spreadsheet

Add these columns to your data:

| Column | Name | Formula (Row 2) |
|--------|------|-----------------|
| J | Traffic_Intensity | `=D2*H2/900` |
| P | Agents_To_Meet_Target | *(unknown - what we're solving for)* |
| Q | Implied_K_Value | `=(P2-J2)/SQRT(J2)` |
| R | Service_Level_Category | `=IF(N2>=0.85,"Excellent",IF(N2>=0.80,"Good",IF(N2>=0.70,"Acceptable","Poor")))` |

#### Step 5: Analyze K-Values by Performance

Filter your data by service level achievement and look at the k-values:

```excel
=AVERAGEIF(R:R, "Good", Q:Q)
=AVERAGEIF(R:R, "Excellent", Q:Q)
```

**Example Analysis:**

| Service Level Achieved | Average K-Value | Interpretation |
|------------------------|-----------------|----------------|
| 70-79% | 1.1 | Understaffed |
| 80-84% | 1.5 | Right-sized for target |
| 85-89% | 1.9 | Slightly overstaffed |
| 90%+ | 2.3 | Overstaffed |

**Your Target:** Find the k-value where 80-85% of intervals meet your service level target.

---

## Method 2: Empirical Testing with Your Data

Use your actual abandonment and service data to back-calculate the ideal k.

### Step-by-Step Process

#### Step 1: Set Up Analysis Template

Create this in Excel using your `call_center_arrival_pattern.csv`:

```
Column A-I:  Your existing data
Column J:    Traffic = (D × H) / 900
Column K:    Test_K_Value = (varies from 1.0 to 3.0)
Column L:    Required_Agents = J + K × SQRT(J)
Column M:    Estimated_Occupancy = J / L
```

#### Step 2: Create K-Value Test Matrix

Test different k-values against your actual performance:

| Interval | Traffic | k=1.0 | k=1.5 | k=2.0 | k=2.5 | Actual SL | Best k |
|----------|---------|-------|-------|-------|-------|-----------|--------|
| Mon 10:00 | 10.73 | 14 | 16 | 17 | 19 | 72% | 1.5-2.0 |
| Mon 11:00 | 10.03 | 13 | 15 | 16 | 18 | 73% | 1.5-2.0 |
| Mon 14:00 | 9.40 | 13 | 14 | 16 | 17 | 75% | 1.5-2.0 |

#### Step 3: Excel Setup for K-Testing

**Create a Data Table:**

1. List k-values in row 1: 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0
2. For each interval, calculate agents needed at each k-value
3. Compare to actual service level achieved

**Formula:**
```excel
=ROUNDUP($J2 + K$1*SQRT($J2), 0)
```

Where:
- J2 = Traffic intensity
- K$1 = k-value from header row

#### Step 4: Statistical Analysis

Calculate correlation between k-values and service level achievement:

```excel
=CORREL(K_Values_Range, Service_Level_Range)
```

Find the **minimum k** where:
```excel
=PERCENTILE(Service_Level_Range, 0.80) >= Target_SL
```

This finds the k where 80% of intervals meet target.

---

## Method 3: Service Level Target-Based Calibration

Start with your target and work backwards using theoretical relationships.

### Theoretical K-Values by Service Level

Based on queueing theory and normal distribution approximations:

| Target Service Level | Answer Time (seconds) | Recommended k | Formula Basis |
|---------------------|----------------------|---------------|---------------|
| 70% in 60 sec | 60 | 1.0 - 1.2 | Φ⁻¹(0.70) × √2 |
| 80% in 90 sec | 90 | 1.4 - 1.6 | Φ⁻¹(0.80) × √2 |
| 80% in 60 sec | 60 | 1.6 - 1.8 | Φ⁻¹(0.80) × √2 × 1.2 |
| 80% in 30 sec | 30 | 1.8 - 2.0 | Φ⁻¹(0.80) × √2 × 1.4 |
| 80% in 20 sec | 20 | 2.0 - 2.3 | Φ⁻¹(0.80) × √2 × 1.6 |
| 90% in 90 sec | 90 | 2.2 - 2.5 | Φ⁻¹(0.90) × √2 |
| 90% in 60 sec | 60 | 2.5 - 2.8 | Φ⁻¹(0.90) × √2 × 1.2 |
| 95% in 30 sec | 30 | 2.8 - 3.2 | Φ⁻¹(0.95) × √2 × 1.4 |

**Φ⁻¹** = Inverse cumulative normal distribution
- Φ⁻¹(0.70) ≈ 0.52
- Φ⁻¹(0.80) ≈ 0.84
- Φ⁻¹(0.90) ≈ 1.28
- Φ⁻¹(0.95) ≈ 1.65

### Quick Selection Guide

For **80% in 90 seconds** (your target):
```
k ≈ 0.84 × √2 = 1.19
```

Add adjustment factors:
- **AHT ratio**: If AHT/Target > 3, add +0.2 to k
- **Traffic variability**: If abandonment > 5%, add +0.1 to k
- **Peak periods**: Add +0.2 during top 20% volume intervals

**Your case:**
- Base k = 1.19
- AHT (270) / Target (90) = 3.0 → Add 0.2
- Abandonment ~5% → Add 0.1
- **Recommended k = 1.5**

---

## Method 4: Regression Analysis (Most Accurate)

Use statistical regression to find optimal k based on your actual data.

### Step-by-Step Excel Implementation

#### Step 1: Prepare Your Dataset

Using your `call_center_arrival_pattern.csv`, create:

| Traffic (X1) | √Traffic (X2) | Actual Agents | Service Level | Good SL (Y) |
|--------------|---------------|---------------|---------------|-------------|
| 10.73 | 3.28 | 16 | 72% | 0 |
| 10.03 | 3.17 | 15 | 73% | 0 |
| 8.21 | 2.87 | 12 | 74% | 0 |
| 7.20 | 2.68 | 12 | 80% | 1 |

Where "Good SL (Y)" = 1 if service level >= 80%, else 0

#### Step 2: Run Multiple Regression

Use Excel's Data Analysis Toolpak:

1. Data → Data Analysis → Regression
2. Input Y Range: Good_SL column
3. Input X Range: Traffic and √Traffic columns
4. Check "Labels" if including headers
5. Click OK

#### Step 3: Interpret Results

You'll get coefficients:
```
Agents_Required = β₀ + β₁(Traffic) + β₂(√Traffic)
```

Where:
- β₁ ≈ 1.0 (should be close to 1, confirming base staffing)
- β₂ = Your empirically-derived k-value

**Example output:**
```
Coefficients:
Intercept:    0.23
Traffic:      0.98
√Traffic:     1.52
```

**Your calibrated k-value = 1.52**

#### Step 4: Validate with R-Squared

Check model fit:
- R² > 0.85 = Excellent fit, trust this k-value
- R² 0.70-0.85 = Good fit, use with minor adjustments
- R² < 0.70 = Poor fit, need more data or different model

---

## Method 5: A/B Testing in Production

Test different k-values in real operations to find optimal balance.

### Controlled Testing Approach

#### Week 1-2: Baseline (k = 1.5)
- Schedule using k = 1.5
- Track actual service level, occupancy, cost
- Measure: SL%, Abandon%, Agent idle time, Cost per call

#### Week 3-4: Test Lower (k = 1.3)
- Schedule using k = 1.3
- Compare metrics to baseline
- If SL drops below 78%, abort test

#### Week 5-6: Test Higher (k = 1.7)
- Schedule using k = 1.7
- Compare cost vs service improvement
- Calculate ROI of extra agents

#### Analysis Template

| K-Value | Avg SL% | Cost/Call | Abandon% | Occupancy% | Score |
|---------|---------|-----------|----------|------------|-------|
| 1.3 | 76% | $3.20 | 7.2% | 82% | Poor |
| 1.5 | 81% | $3.45 | 4.8% | 75% | **Best** |
| 1.7 | 86% | $3.72 | 3.1% | 68% | Over |

**Score Formula:**
```
Score = (SL% / Target_SL) × (1 - Abandon%) × (Cost_Baseline / Cost_Actual)
```

Choose k with highest score that meets minimum SL threshold.

---

## Practical Calibration Workflow for Your Data

### Quick Start: 3-Step Calibration

#### Step 1: Initial K from Theory
For 80% in 90 seconds with AHT ~270 seconds:
```
k_initial = 1.5
```

#### Step 2: Calculate Agents Needed
Apply to your peak Monday period:

| Interval | Traffic | k=1.5 Agents | k=1.7 Agents | k=2.0 Agents |
|----------|---------|--------------|--------------|--------------|
| 10:00-10:15 | 10.73 | 16 | 16 | 17 |
| 11:00-11:15 | 10.03 | 15 | 15 | 16 |
| 14:00-14:15 | 9.40 | 14 | 15 | 16 |

#### Step 3: Validate Against Actual Performance
Compare to your actual abandonment rates:

- If abandon rate 0-3%: **k is too high** (overstaffed)
- If abandon rate 3-5%: **k is optimal** ✓
- If abandon rate 5-8%: **k is too low** (understaffed)
- If abandon rate >8%: **k is much too low**

**Your data shows:**
- Monday 10:00: 5.71% abandon → k=1.5 is slightly low, try k=1.6
- Monday 11:00: 6.25% abandon → k=1.5 is slightly low, try k=1.6
- Monday 14:00: 6.67% abandon → k=1.5 is too low, try k=1.7

**Calibrated result: k = 1.6 to 1.7 for your operation**

---

## Advanced: K-Value by Time of Day

Different intervals may need different k-values:

### Morning Ramp-Up (8:00-10:00)
- **Characteristics:** Unpredictable volume, queue buildup
- **Recommended k:** 1.7 - 2.0 (conservative)

### Peak Hours (10:00-14:00)
- **Characteristics:** High volume, steady arrival pattern
- **Recommended k:** 1.5 - 1.7 (balanced)

### Afternoon Steady (14:00-16:00)
- **Characteristics:** Moderate volume, predictable
- **Recommended k:** 1.4 - 1.6 (efficient)

### Evening Wind-Down (16:00-17:00)
- **Characteristics:** Declining volume, harder to adjust staffing
- **Recommended k:** 1.6 - 1.8 (buffer for inflexibility)

### Weekend/Low Volume
- **Characteristics:** Very low traffic (<3 Erlangs)
- **Recommended:** Use minimum staffing rules instead of square root

---

## K-Value Adjustment Factors

Fine-tune your base k-value with these multipliers:

### Call Type Complexity
```
k_adjusted = k_base × Complexity_Factor
```

| Call Type | Complexity Factor |
|-----------|------------------|
| Simple FAQ | 0.9 |
| Standard support | 1.0 |
| Technical support | 1.1 |
| Sales/retention | 1.2 |
| VIP/escalations | 1.3 |

### Traffic Volatility
Calculate coefficient of variation (CV):
```
CV = StdDev(Calls) / Mean(Calls)
```

| CV | Volatility | K Adjustment |
|----|------------|--------------|
| < 0.2 | Low | -0.1 |
| 0.2-0.4 | Moderate | 0.0 |
| 0.4-0.6 | High | +0.1 |
| > 0.6 | Very High | +0.2 |

### Abandonment Sensitivity
```
If Abandonment_Rate > 5%: k = k + 0.2
If Abandonment_Rate > 10%: k = k + 0.4
```

### Cost Pressure
```
If Labor_Cost > Budget × 1.1: k = k - 0.1 (with caution)
If Customer_Value > $500: k = k + 0.2
```

---

## Excel Template for K-Calibration

Here's a complete Excel formula set:

```excel
' Column J: Traffic
=D2*H2/900

' Column K: Base K-Value (enter manually: 1.5)
=1.5

' Column L: Adjusted K for Volatility
=K2+IF(STDEV(D:D)/AVERAGE(D:D)>0.4, 0.1, 0)

' Column M: Adjusted K for Abandon Rate
=L2+IF(G2>0.05, 0.2, 0)

' Column N: Final Calibrated K
=M2

' Column O: Required Agents
=ROUNDUP(J2+N2*SQRT(J2), 0)

' Column P: Predicted Service Level
=IF(O2<=J2, 0, 1-(Erlang_C_Prob*EXP(-((O2-J2)*(90/H2)))))

' Column Q: Meets Target? (80%)
=IF(P2>=0.80, "YES", "NO")
```

---

## Validation Checklist

Before finalizing your k-value:

- [ ] **Service Level Test**: 80%+ of intervals meet target
- [ ] **Cost Test**: Labor cost within budget
- [ ] **Occupancy Test**: Average occupancy 70-85%
- [ ] **Abandon Test**: Abandonment rate < 5%
- [ ] **Peak Test**: Handles highest volume days
- [ ] **Variance Test**: Consistent across different times
- [ ] **Trend Test**: Works for increasing volume
- [ ] **Stakeholder Test**: Management comfortable with risk/cost balance

---

## Recommended K-Values Summary

Based on your data (80% in 90 seconds, AHT ~270 sec, 3-7% abandonment):

| Scenario | Recommended K | Rationale |
|----------|---------------|-----------|
| **Current baseline** | 1.6 | Matches your 4-6% abandonment pattern |
| **Cost optimization** | 1.4 | 10% less staff, accept 75-78% SL |
| **Service optimization** | 1.8 | 85-88% SL, 2-3% abandonment |
| **Peak hours only** | 1.7 | Extra buffer when volume highest |
| **Off-peak hours** | 1.4 | Efficient when predictable |
| **Monday (busiest)** | 1.7 | Account for weekly peak |
| **Saturday (lightest)** | 1.5 | Less variability, lower buffer |

---

## Next Steps

1. **Calculate your historical k-values** using Method 1
2. **Test k = 1.6** across all your intervals
3. **Monitor actual vs predicted** for 2 weeks
4. **Refine by time of day** if needed
5. **Document final k-values** in your staffing guidelines

---

## Quick Reference: K-Value Decision Tree

```
Start: What's your primary goal?

├─ Minimize Cost
│  └─ Can you accept 75-78% SL?
│     ├─ Yes → k = 1.3 to 1.4
│     └─ No → k = 1.5

├─ Balance Cost & Service (80% SL target)
│  └─ What's your AHT/Target ratio?
│     ├─ < 2.0 → k = 1.4
│     ├─ 2.0-3.5 → k = 1.5 to 1.6
│     └─ > 3.5 → k = 1.7 to 1.8

├─ Maximize Service Quality
│  └─ What SL do you need?
│     ├─ 85% → k = 1.9
│     ├─ 90% → k = 2.3
│     └─ 95% → k = 2.8

└─ Minimize Abandonment
   └─ Current abandon rate?
      ├─ < 3% → k is adequate
      ├─ 3-5% → increase k by 0.1
      ├─ 5-8% → increase k by 0.2
      └─ > 8% → increase k by 0.3+
```

**Your scenario: AHT/Target = 3.0, 5-7% abandon → k = 1.6 to 1.7**
