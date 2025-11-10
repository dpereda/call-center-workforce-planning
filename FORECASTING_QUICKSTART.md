# Forecasting Quick Start Guide
## Get Up and Running in 15 Minutes

This guide gets you forecasting call center volumes fast using Excel's built-in functions. No macros, no complex setup.

---

## Prerequisites

- ✅ Excel 2016 or newer (Windows, Mac, or Office 365)
- ✅ At least 12 months of historical call data
- ✅ Data in format: Date | Time | Calls_Offered

---

## Step 1: Prepare Your Data (5 minutes)

### Open Excel and Set Up Columns

```
| A: Date       | B: Time    | C: Calls_Offered | D: Day_of_Week |
|---------------|------------|------------------|----------------|
| 2024-01-01    | 08:00-08:15| 42               | =TEXT(A2,"dddd") |
| 2024-01-01    | 08:15-08:30| 38               | =TEXT(A3,"dddd") |
```

### Add Helper Column

**Column D - Day of Week:**
```excel
=TEXT(A2,"dddd")
```

Drag down to fill all rows.

**Why:** Helps identify weekly patterns later.

---

## Step 2: Create Your First Forecast (3 minutes)

### Use FORECAST.ETS

In the first row after your historical data (e.g., row 1001):

```excel
=FORECAST.ETS(A1001, $C$2:$C$1000, $A$2:$A$1000, 96, 1, 1)
```

**What this means:**
- `A1001`: The future date you're forecasting
- `$C$2:$C$1000`: Your historical call volumes (fixed reference)
- `$A$2:$A$1000`: Your historical dates (fixed reference)
- `96`: Daily seasonality (for 15-min intervals: 24 hours × 4 = 96)
- `1`: Fill missing data
- `1`: Average duplicate timestamps

### Drag Down

Copy the formula down for as many periods as you need (typically 1-4 weeks).

**Done!** You now have a forecast.

---

## Step 3: Check Your Accuracy (5 minutes)

### Calculate MAPE (Mean Absolute Percentage Error)

**Add these columns to your data:**

**Column E - Absolute Percent Error:**
```excel
=ABS(C2-D2)/ABS(C2)*100
```

Where:
- C2 = Actual calls
- D2 = Forecasted calls (from Step 2)

**Column F - MAPE Summary:**
```excel
=AVERAGE(E2:E1000)
```

### Interpret Your MAPE

| Your MAPE | Meaning | Action |
|-----------|---------|--------|
| < 5% | Excellent | Keep going! |
| 5-7% | Good | Minor tweaks needed |
| 7-10% | Acceptable | Review methodology |
| > 10% | Poor | Need more data or different method |

---

## Step 4: Visualize (2 minutes)

### Create a Simple Chart

1. Select your data (Date, Actual, Forecast columns)
2. **Insert** → **Line Chart**
3. Format:
   - Blue line: Actual
   - Orange dotted line: Forecast
   - X-axis: Date/Time
   - Y-axis: Call Volume

**You now have a visual forecast to share with management!**

---

## Quick Adjustments for Special Events

### Add a Buffer for Known Events

If you know there's a marketing campaign next week:

```excel
// Original forecast
=FORECAST.ETS(A1001, $C$2:$C$1000, $A$2:$A$1000, 96, 1, 1)

// Adjusted for 20% campaign lift
=FORECAST.ETS(A1001, $C$2:$C$1000, $A$2:$A$1000, 96, 1, 1) * 1.20
```

### Common Adjustments

| Event | Typical Adjustment | Formula Multiplier |
|-------|-------------------|-------------------|
| Email campaign | +15-25% | × 1.20 |
| Holiday (before) | +20-40% | × 1.30 |
| Holiday (closed) | -100% | × 0 |
| Billing cycle | +10-15% | × 1.12 |
| Product launch | +30-50% | × 1.40 |

---

## Common Issues & Quick Fixes

### Issue 1: #VALUE! Error

**Cause:** Dates aren't recognized as dates

**Fix:**
```excel
// Convert text to date
=DATEVALUE(A2) + TIMEVALUE(B2)
```

### Issue 2: Forecast Looks Flat

**Cause:** Not enough data or seasonality not detected

**Fix:**
- Add more historical data (need minimum 24 months)
- Try different seasonality value (48, 96, or 168)

### Issue 3: Huge Spikes in Forecast

**Cause:** Outliers in historical data

**Fix:**
- Identify and remove one-time events
- Filter out system outages, data errors

---

## Next Steps

### To Improve Your Forecast:

1. **Add More Data**
   - Minimum: 12 months
   - Better: 24 months
   - Best: 36+ months

2. **Track Accuracy Weekly**
   - Calculate MAPE every Monday
   - Identify problematic time periods
   - Adjust methodology as needed

3. **Create Event Calendar**
   - List all special events (campaigns, holidays, launches)
   - Note impact (% increase/decrease)
   - Apply adjustments to forecast

4. **Forecast AHT Too**
   - Don't assume Average Handle Time is constant
   - Use same FORECAST.ETS method on AHT data
   - Multiply Volume × AHT for true workload

5. **Automate Reporting**
   - Weekly accuracy dashboard
   - Month-over-month comparison
   - Share with stakeholders

---

## Copy-Paste Formulas

### Complete Formula Set

```excel
// Helper: Day of Week
=TEXT(A2,"dddd")

// Helper: Period Number
=ROW()-1

// Forecast (15-min intervals, daily pattern)
=FORECAST.ETS(A1001, $C$2:$C$1000, $A$2:$A$1000, 96, 1, 1)

// Absolute Percent Error (APE)
=ABS(C2-D2)/ABS(C2)*100

// MAPE
=AVERAGE(E2:E1000)

// Confidence Interval (Upper Bound)
=D2 + FORECAST.ETS.CONFINT(A2, $C$2:$C$1000, $A$2:$A$1000, 0.95, 96)

// Confidence Interval (Lower Bound)
=D2 - FORECAST.ETS.CONFINT(A2, $C$2:$C$1000, $A$2:$A$1000, 0.95, 96)

// Event Adjustment (if date is in Event List)
=IF(COUNTIF(EventDates,A2)>0, D2*1.25, D2)
```

---

## Seasonality Cheat Sheet

| Your Data Interval | Seasonality Value | Pattern Detected |
|-------------------|------------------|------------------|
| 5-minute | 288 | Daily (24 × 12) |
| 15-minute | 96 | Daily (24 × 4) |
| 30-minute | 48 | Daily (24 × 2) |
| Hourly | 24 | Daily |
| Daily | 7 | Weekly |
| Weekly | 52 | Yearly |
| Monthly | 12 | Yearly |

**Tip:** If unsure, let Excel auto-detect by omitting the seasonality parameter:
```excel
=FORECAST.ETS(A1001, $C$2:$C$1000, $A$2:$A$1000)
```

---

## 5-Minute Accuracy Check

### Quick Dashboard

Create this simple table:

| Metric | Formula | Your Result | Target |
|--------|---------|-------------|--------|
| MAPE | `=AVERAGE(APE_column)` | ___% | <7% |
| Best Day | `=INDEX(Days, MATCH(MIN(MAPE_by_day), MAPE_by_day, 0))` | _____ | - |
| Worst Day | `=INDEX(Days, MATCH(MAX(MAPE_by_day), MAPE_by_day, 0))` | _____ | - |

**Conditional formatting:** Green if <7%, Yellow if 7-10%, Red if >10%

---

## Alternative: Forecast Sheet (Automated)

### Excel's Built-In Tool

**For the absolute easiest method:**

1. Select your data (Date and Calls columns)
2. **Data tab** → **Forecast Sheet**
3. Set:
   - Forecast End: 4 weeks from today
   - Confidence Interval: 95%
   - Seasonality: Auto-detect
4. Click **Create**

**Result:** Excel creates a complete forecast with chart automatically!

**Pros:**
- Zero formulas needed
- Beautiful visualization
- Confidence intervals included

**Cons:**
- Can't easily adjust for events
- New sheet each time (not dynamic)
- Limited customization

---

## When You're Ready for More

### Read the Full Guide

For advanced techniques, see `call_center_forecasting_guide.md`:
- Seasonal decomposition method
- Handling special events
- Multiple forecasting methods comparison
- When to upgrade to WFM software

### Practice Dataset

Use `call_center_arrival_pattern.csv` in this repository:
- 1 week of realistic call data
- 15-minute intervals
- Perfect for testing formulas

---

## Summary: The Absolute Minimum

If you only do these 3 things:

1. **Use FORECAST.ETS**
   ```excel
   =FORECAST.ETS(future_date, historical_values, historical_dates, 96, 1, 1)
   ```

2. **Measure MAPE**
   ```excel
   =AVERAGE(ABS((Actual-Forecast)/Actual)*100)
   ```

3. **Update Monthly**
   - Add latest data
   - Rerun forecast
   - Track accuracy trends

**You'll be 80% of the way to good forecasting.**

The rest is optimization.

---

## Need Help?

**Common Questions:**

**Q: My forecast is way off. What do I do?**
A: Check these:
- Do you have at least 12 months of data?
- Are there outliers (system outages, etc.)?
- Is seasonality value correct for your data?
- Have business patterns changed recently?

**Q: Can I forecast hourly instead of 15-minute intervals?**
A: Yes! Change seasonality to 24 (24 hours in a day).

**Q: What if I don't have Excel 2016+?**
A: Use Seasonal Decomposition method (see full guide).

**Q: How far ahead can I forecast?**
A: FORECAST.ETS works best for 1-4 weeks ahead. Beyond that, use simpler trend methods.

**Q: Should I forecast weekends separately?**
A: Yes, if weekend patterns are very different. Create separate models for weekday vs weekend.

---

## Success Checklist

After following this guide, you should have:

- [  ] Forecast for next 1-4 weeks
- [  ] MAPE calculated and tracked
- [  ] Simple chart showing actual vs forecast
- [  ] Understanding of your accuracy level
- [  ] Plan for monthly updates

**Congratulations! You're now forecasting like a pro.** 🎉

---

*For questions or improvements to this guide, see the repository:*
*https://github.com/dpereda/call-center-workforce-planning*

*Last updated: November 2025*
