# Service Level Calculator - User Guide

## Overview

The **Service Level Calculator** is an Excel-based tool that helps you determine what service levels you'll actually achieve based on your agent schedule and shrinkage rate. This tool **reverses** the typical Erlang C calculation:

**Traditional Flow:** Forecast → Calculate Required Agents
**Service Level Calculator:** Agent Schedule + Shrinkage → Calculate Achievable Service Levels

## Quick Start

1. **Open the file:** `erlang_c_staffing_forecast.xlsx`
2. **Navigate to worksheet:** `Schedule_Service_Level`
3. **Set your shrinkage rate:** Cell `E4` (default: 25%)
4. **Enter your agent schedule:** Column `D` - "Scheduled Agents"
5. **Review the outputs:** Service Level %, ASA, Occupancy, Staffing Gap

## Worksheet Structure

### Input Section (Yellow Background)

| Column | Name | Description | User Action |
|--------|------|-------------|-------------|
| **E4** | Shrinkage Rate | Single percentage applied to all intervals | **EDIT THIS** - Enter your expected shrinkage (typically 25-30%) |
| **D** | Scheduled Agents | Number of agents scheduled for each interval | **EDIT THIS** - Enter your staffing plan |

### Calculation Section (Gray Background)

These columns are automatically calculated - do not edit:

| Column | Name | Formula | Purpose |
|--------|------|---------|---------|
| **E** | Net Agents | `Scheduled × (1 - Shrinkage)` | Actual available agents after shrinkage |
| **F** | Calls Offered | From forecast data | Expected call volume |
| **G** | AHT (sec) | From forecast data | Average Handle Time |
| **H** | Traffic (Erlangs) | `(Calls × AHT) / 900` | Traffic intensity for 15-min interval |
| **I** | Req. Agents | From forecast data | Optimal agents needed (for comparison) |

### Output Section

| Column | Name | Description | Target |
|--------|------|-------------|--------|
| **J** | Erlang C Prob. | Probability that a caller will wait | Lower is better |
| **K** | Service Level % | % of calls answered within 90 seconds | **≥ 80%** |
| **L** | ASA (sec) | Average Speed of Answer | < 90 seconds |
| **M** | Occupancy % | Agent utilization rate | **75-85%** |
| **N** | Staffing Gap | Net Agents - Required Agents | 0 = perfect staffing |

## Understanding Shrinkage

### What is Shrinkage?

**Shrinkage** is the percentage of time agents are scheduled but not available to take calls.

### Typical Shrinkage Components

| Component | Typical % | Description |
|-----------|-----------|-------------|
| **Breaks** | 12-15% | Morning/afternoon breaks, lunch |
| **Training** | 5% | Ongoing coaching and skill development |
| **Meetings** | 3% | Team huddles, 1-on-1s, department meetings |
| **Absenteeism** | 5-7% | Sick leave, personal days |
| **System/Technical** | 2-3% | Login issues, system downtime |
| **Total** | **25-30%** | Industry standard range |

### Shrinkage Calculation

```
Net Agents = Scheduled Agents × (1 - Shrinkage Rate)

Example:
- Scheduled Agents: 12
- Shrinkage Rate: 25%
- Net Agents: 12 × (1 - 0.25) = 12 × 0.75 = 9

You need to schedule 12 agents to have 9 actually available.
```

### Reverse Calculation (Gross Staffing)

If you know you need **9 net agents** and have **25% shrinkage**:

```
Scheduled Agents = Net Agents / (1 - Shrinkage)
Scheduled Agents = 9 / 0.75 = 12
```

## Using the Calculator - Step by Step

### Step 1: Set Your Shrinkage Rate

1. Click on cell **E4**
2. Enter your shrinkage percentage (e.g., `25%` or `0.25`)
3. Typical range: 25-30%
4. This applies uniformly to all intervals

### Step 2: Enter Your Agent Schedule

1. Go to column **D** (Scheduled Agents)
2. For each time interval, enter the number of agents you plan to schedule
3. This represents your **gross staffing** (before shrinkage)
4. The tool automatically calculates net agents in column E

**Example Schedule:**
```
Time           Scheduled Agents
08:00-08:15    10
08:15-08:30    10
08:30-08:45    12
08:45-09:00    12
09:00-09:15    14
...
```

### Step 3: Review Service Level Metrics

Once you've entered your schedule, review column **K** (Service Level %):

- **Green cells:** Meeting 80% target ✓
- **Red cells:** Below 80% target ✗ - Need more agents

### Step 4: Analyze Occupancy

Review column **M** (Occupancy %):

- **< 70% (Blue):** Overstaffed - agents idle too much
- **75-85% (Normal):** Optimal range - good balance
- **> 85% (Orange):** Overstaffed or high stress - burnout risk

### Step 5: Check Staffing Gaps

Review column **N** (Staffing Gap):

- **Positive number:** You have MORE agents than needed
- **Zero:** Perfect staffing match
- **Negative number (Red):** You're SHORT agents - service will suffer

### Step 6: Review Summary Dashboard

Scroll to the bottom of the worksheet to see overall KPIs:

| Metric | What It Means | Action If... |
|--------|---------------|--------------|
| **Average Service Level** | Overall performance | < 80%: Add more agents |
| **Intervals Below 80%** | Number of problem periods | > 5: Review those specific times |
| **Average Occupancy** | Agent utilization | > 85%: Risk of burnout |
| **Total Staffing Gap** | Overall surplus/deficit | Negative: Need more total staff |

## Practical Workflows

### Workflow 1: Validate an Existing Schedule

**Use Case:** You've already created an agent schedule and want to know if it will meet service level targets.

1. Enter your shrinkage rate (e.g., 25%)
2. Copy your schedule into column D
3. Review Service Level % column - identify intervals below 80%
4. Adjust schedule for problem intervals
5. Re-check until all intervals meet target

### Workflow 2: Build a Schedule from Scratch

**Use Case:** You have a forecast and need to create a staffing plan.

1. Start with column I (Required Agents) - this is your baseline
2. Calculate gross staffing: `Required / (1 - Shrinkage)`
3. Enter these values in column D
4. Review Service Level % to verify
5. Fine-tune based on occupancy and gaps

### Workflow 3: Test Different Shrinkage Scenarios

**Use Case:** You want to understand impact of different shrinkage assumptions.

1. Enter your schedule once in column D
2. Test different shrinkage rates in cell E4:
   - 20% (optimistic)
   - 25% (typical)
   - 30% (conservative)
3. Compare Service Level % results for each scenario
4. Choose the scenario that balances cost and service

### Workflow 4: Optimize for Target Occupancy

**Use Case:** You want to maintain 80% occupancy while meeting service levels.

1. Enter initial schedule in column D
2. Review Occupancy % (column M)
3. For intervals with low occupancy (< 75%): reduce scheduled agents
4. For intervals with high occupancy (> 85%): add scheduled agents
5. Verify Service Level % doesn't drop below 80%

## Interpreting Results

### Service Level Achievement

| Result | Interpretation | Action |
|--------|----------------|--------|
| **90-100%** | Excellent service, may be overstaffed | Consider reducing agents to optimize cost |
| **80-89%** | Meeting target, good balance | Maintain current staffing |
| **70-79%** | Below target, customers waiting | Add agents during these intervals |
| **< 70%** | Poor service, long waits | Immediate staffing increase needed |

### Average Speed of Answer (ASA)

| ASA | Service Quality | Customer Experience |
|-----|-----------------|---------------------|
| **< 20 sec** | Excellent | Immediate answer |
| **20-60 sec** | Good | Acceptable wait |
| **60-90 sec** | Fair | Approaching limit |
| **> 90 sec** | Poor | Unacceptable wait |

### Occupancy Rate

| Occupancy | Utilization | Agent Experience | Recommendation |
|-----------|-------------|------------------|----------------|
| **< 70%** | Low | Too much idle time | Reduce staff or reassign |
| **70-75%** | Moderate | Good work-life balance | Acceptable |
| **75-85%** | Optimal | Busy but sustainable | **Target range** |
| **85-90%** | High | Stressful, limited breaks | Monitor for burnout |
| **> 90%** | Very High | Unsustainable | Add staff immediately |

## Troubleshooting

### Issue: "Need More" appears in Erlang C column

**Cause:** Net agents ≤ traffic intensity (mathematically impossible to serve calls)

**Solution:**
- Increase scheduled agents in column D
- Reduce shrinkage rate if realistic
- Verify forecast data is correct

### Issue: Service Level shows 0%

**Cause:** Insufficient net agents relative to traffic

**Solution:**
- Check that Scheduled Agents (column D) > Required Agents (column I)
- Account for shrinkage properly
- Add more scheduled agents

### Issue: Occupancy shows > 100%

**Cause:** Net agents < traffic intensity

**Solution:**
- This means queues will grow indefinitely
- Immediately increase scheduled agents
- Review your shrinkage assumptions

### Issue: All service levels are 100%

**Possible Causes:**
1. Significantly overstaffed (verify column N - should show large positive gaps)
2. Forecast data has very low call volume
3. Shrinkage rate set too low

**Solution:**
- Review if this is realistic given your budget
- Consider reducing staff if appropriate
- Optimize for target 80% service level, not 100%

## Advanced Tips

### Tip 1: Intraday Scheduling

For maximum efficiency:
1. Schedule fewer agents during low-traffic periods (early morning, late afternoon)
2. Schedule more agents during peaks (mid-morning, early afternoon)
3. Use the calculator to find the minimum staff needed per interval

### Tip 2: Break Planning

Consider scheduling breaks during naturally low-volume periods:
1. Identify intervals with lower call volume in column F
2. Schedule breaks during these times
3. This naturally reduces effective agents when demand is lower

### Tip 3: Cross-Training

If you have multi-skilled agents:
1. Lower effective shrinkage (agents can switch between queues)
2. Test with 20-23% shrinkage instead of 25%
3. Verify service levels improve with same gross staff

### Tip 4: Holiday Planning

For holidays or special events:
1. Update forecast data with expected call patterns
2. Adjust staffing in column D accordingly
3. May need higher shrinkage due to time-off requests

### Tip 5: Continuous Improvement

Monthly review process:
1. Compare actual service levels vs. calculator predictions
2. Adjust K-values in forecast if predictions are off
3. Update shrinkage assumptions based on actual data
4. Recalibrate and re-run

## Integration with Other Tools

### From Forecasting to Scheduling

1. **Start:** Run Erlang C Staffing Forecast
2. **Get:** Required_Agents column (optimal staffing)
3. **Adjust:** Multiply by `1 / (1 - Shrinkage)` to get gross staffing
4. **Input:** Enter into Service Level Calculator column D
5. **Validate:** Verify service levels meet targets

### Exporting Results

To use results in other tools:
1. Copy columns A-N to new worksheet
2. Save as CSV: `File → Save As → CSV`
3. Import into WFM software, BI tools, or reporting systems

## Formulas Reference

### Key Excel Formulas Used

**Net Agents:**
```excel
=ROUND(D8*(1-$E$4),1)
```

**Traffic Intensity:**
```excel
=(G8*H8)/900
```

**Erlang C Probability:**
```excel
=IF(E8<=I8,"Need More",
(POWER(E8,I8)/FACT(E8)*(E8/(E8-I8)))/
(SUMPRODUCT(POWER(I8,ROW(INDIRECT("0:"&(E8-1))))/
FACT(ROW(INDIRECT("0:"&(E8-1)))))+
(POWER(E8,I8)/FACT(E8)*(E8/(E8-I8)))))
```

**Service Level (80/90):**
```excel
=IF(E8<=I8,0,
IF(ISNUMBER(J8),1-(J8*EXP(-((E8-I8)*(90/H8)))),0))
```

**ASA (seconds):**
```excel
=IF(E8<=I8,"Need More",
IF(ISNUMBER(J8),(J8*H8)/(E8-I8),0))
```

**Occupancy:**
```excel
=IF(E8>0,I8/E8,0)
```

**Staffing Gap:**
```excel
=E8-F8
```

## FAQs

**Q: Can I use different shrinkage rates for different times of day?**
A: Currently, the tool uses a single rate. For variable shrinkage, you would need to manually calculate net agents and enter them directly.

**Q: What if I have part-time agents?**
A: Enter fractional values (e.g., 10.5 agents) in column D. The calculator handles decimals.

**Q: Can I calculate for multiple days at once?**
A: Yes! Just extend the data rows. Copy the formulas down and update the date/time intervals.

**Q: Should I target exactly 80% service level?**
A: 80% is the industry minimum. Aim for 82-85% to have a buffer for unexpected spikes.

**Q: What if my actual shrinkage varies day to day?**
A: Use an average shrinkage rate, or create separate worksheets for different day types (Monday, Tuesday, etc.).

**Q: Can I calculate service level for different targets (e.g., 90/120)?**
A: Yes, but you'll need to modify the formula. Change "90" in the Service Level formula to your target seconds.

## Related Resources

- **ERLANG_C_EXCEL_FORMULAS_GUIDE.txt** - Complete Erlang C formula reference
- **square_root_staffing_rule_explained.md** - Theory behind staffing calculations
- **k_value_calibration_guide.md** - How to optimize forecasting accuracy
- **erlang_c_staffing_forecast.csv** - Original forecast data with required agents

## Support

For questions or issues:
1. Review this guide thoroughly
2. Check the Troubleshooting section
3. Verify your forecast data is accurate
4. Consult the formula reference documents

---

**Last Updated:** 2025-11-10
**Version:** 1.0
**Tool:** Service Level Calculator for Call Center Workforce Planning
