# Call Center Workforce Planning & Staffing Optimization

A comprehensive toolkit for call center workforce planning using **Erlang C** queueing theory, **Square Root Staffing** rules, and data-driven optimization techniques.

## 📊 Overview

This repository provides practical tools and guides for:
- **Forecasting call volumes** with realistic arrival patterns
- **Calculating optimal staffing levels** using Erlang C formulas
- **Calibrating staffing models** to your historical data
- **Understanding queueing theory** with clear explanations
- **Building Excel-based workforce planning** tools

Perfect for call center managers, workforce planners, operations analysts, and anyone working with customer service operations.

## 🚀 Quick Start

### Option 1: Use the Pre-Built Excel Forecast
1. Open `erlang_c_staffing_forecast.xlsx`
2. Review the calculated staffing requirements
3. Adjust the **k-value** (column K) based on your service level targets
4. Use Goal Seek to optimize individual intervals

### Option 2: Build Your Own Model
1. Start with your call data in the format of `call_center_arrival_pattern.csv`
2. Follow the formulas in `ERLANG_C_EXCEL_FORMULAS_GUIDE.txt`
3. Calibrate your k-value using `k_value_calibration_guide.md`
4. Apply the staffing calculations to your schedule

### Option 3: Generate Sample Data
```bash
python generate_annual_call_data.py
```
This creates a full year of realistic call center data for testing and learning.

## 📁 Repository Structure

```
callcenterexample/
├── README.md                                    # This file
├── LICENSE                                      # MIT License
│
├── 📊 Data Files
│   ├── call_center_arrival_pattern.csv         # Sample week of call data
│   ├── call_center_annual_data.csv             # Full year sample data
│   ├── erlang_c_staffing_forecast.csv          # Calculated staffing needs
│   └── erlang_c_staffing_forecast.xlsx         # Excel workbook with formulas
│
├── 📖 Documentation
│   ├── ERLANG_C_EXCEL_FORMULAS_GUIDE.txt       # Complete Excel formula guide
│   ├── square_root_staffing_rule_explained.md  # Theory and mathematics
│   └── k_value_calibration_guide.md            # Calibration methodology
│
├── 🔧 Tools
│   └── generate_annual_call_data.py            # Sample data generator
│
└── .gitignore
```

## 📈 Sample Data Format

The call center data includes 15-minute interval granularity:

| Column | Description |
|--------|-------------|
| Day | Day of week |
| Date | Date of interval |
| Time_Interval | 15-minute time block |
| Calls_Offered | Total incoming calls |
| Calls_Answered | Calls handled by agents |
| Calls_Abandoned | Calls where customer hung up |
| Abandonment_Rate_% | Percentage of abandoned calls |
| Average_Handle_Time_Seconds | AHT in seconds |
| Average_Speed_of_Answer_Seconds | ASA in seconds |

## 🧮 Key Formulas

### Traffic Intensity (Erlangs)
```
Traffic = (Calls_Offered × AHT_Seconds) / Interval_Seconds
```

### Square Root Staffing Rule
```
Required_Agents = Traffic + k × √Traffic
```
Where k typically ranges from 1.4 to 2.0 depending on service level targets.

### Service Level Target
Standard industry target: **80% of calls answered within 90 seconds** (80/90)

## 📊 Key Findings from Sample Data

### Weekly Staffing Requirements (Peak)
| Day | Peak Agents Needed | Peak Time |
|-----|-------------------|-----------|
| Monday | 16-17 agents | 10:00-10:15 |
| Tuesday | 14 agents | 10:00-10:15 |
| Wednesday | 13 agents | 10:00-10:15 |
| Thursday | 14 agents | 10:00-10:15 |
| Friday | 12 agents | 10:00-11:15 |
| Saturday | 9 agents | 10:00-10:15 |

### Recommended K-Values
- **Morning ramp (08:00-10:00):** k = 1.7 (handle uncertainty)
- **Peak hours (10:00-14:00):** k = 1.6 (balanced)
- **Afternoon steady (14:00-17:00):** k = 1.6 (efficient)
- **Saturday/low volume:** k = 1.5 (predictable)

## 📚 Documentation Highlights

### 1. Square Root Staffing Rule
Learn the mathematics and intuition behind the most practical workforce planning formula:
- Why square root works (economies of scale)
- When it's accurate vs. when to use full Erlang C
- Calibrating k-values for different service levels

### 2. K-Value Calibration
Five different methods to find your optimal k-value:
- **Method 1:** Reverse engineering from historical data
- **Method 2:** Empirical testing with actual performance
- **Method 3:** Service level target-based calibration
- **Method 4:** Regression analysis (most accurate)
- **Method 5:** A/B testing in production

### 3. Erlang C Formulas
Complete Excel implementation guide including:
- Traffic intensity calculations
- Erlang C probability of waiting
- Average Speed of Answer (ASA)
- Service level achievement
- Occupancy and utilization

## 🎯 Use Cases

### For Call Center Managers
- Forecast staffing needs for upcoming weeks
- Justify headcount requests with data
- Balance cost efficiency with service quality
- Plan for seasonal volume changes

### For Workforce Planners
- Build optimal shift schedules
- Calculate shrinkage and gross staffing
- Handle peak periods and special events
- Multi-skill routing optimization

### For Operations Analysts
- Analyze historical performance
- Identify optimization opportunities
- Build business cases for investments
- Create executive dashboards

### For Students & Researchers
- Learn queueing theory with practical examples
- Understand Erlang C mathematics
- Study real-world call center patterns
- Build workforce optimization models

## 🔬 Methodology

### Data Generation
Sample data is generated using research-backed patterns:
- Peak hours: 10am-12pm and 2-3pm
- Monday ~20% higher volume than mid-week
- 40% of hourly calls in first 15 minutes
- Abandonment: 2-5% well-staffed, up to 10-15% under stress
- Average Handle Time: 4.5 minutes (260-280 seconds)

### Staffing Calculations
Based on industry-standard **Erlang C** queueing model:
- M/M/c queue (Markovian arrivals, exponential service, c servers)
- Assumes: No abandonment (or use Erlang X for abandonment)
- Infinite queue capacity
- FCFS (First Come First Served) discipline

### Validation
Models validated against:
- Industry benchmarks (80/20, 80/90 service levels)
- Real call center data patterns
- Academic queueing theory research
- Workforce management best practices

## 🛠️ Tools & Technologies

- **Excel/CSV:** Primary delivery format for universal compatibility
- **Python:** Data generation and analysis scripts
- **Markdown:** Documentation and guides
- **Erlang C:** Queueing theory foundation
- **Statistical Methods:** Regression, correlation, validation

## 📖 Learning Path

**Beginner (Start Here):**
1. Read `square_root_staffing_rule_explained.md`
2. Open `erlang_c_staffing_forecast.xlsx`
3. Experiment with different k-values
4. Understand the ASA formula breakdown

**Intermediate:**
1. Read `ERLANG_C_EXCEL_FORMULAS_GUIDE.txt`
2. Build your own staffing model from scratch
3. Use Goal Seek to optimize intervals
4. Calculate shrinkage and create shift schedules

**Advanced:**
1. Read `k_value_calibration_guide.md`
2. Calibrate using your historical data (Method 4 - Regression)
3. Implement Erlang X for abandonment scenarios
4. Build sensitivity analysis and optimization models

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- Additional sample datasets (retail, healthcare, tech support)
- Erlang X (abandonment) formulas and guides
- Multi-skill routing optimization
- Real-time adherence tracking
- Shift schedule optimization algorithms
- Interactive web-based calculators

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Erlang C formula:** Based on A.K. Erlang's groundbreaking work (1917)
- **Square Root Staffing:** Modern approximation from queueing theory research
- **Call patterns:** Synthesized from industry research and real-world observations
- **Best practices:** Compiled from workforce management industry standards

## 📞 Support & Questions

For questions about:
- **Formula usage:** See the Excel formulas guide
- **Calibration:** See the k-value calibration guide
- **Theory:** See the square root staffing explanation
- **Implementation:** Review the sample Excel workbook

## 🔗 Related Resources

- [Queueing Theory](https://en.wikipedia.org/wiki/Queueing_theory)
- [Erlang C Calculator](https://www.callcentrehelper.com/tools/erlang-calculator/)
- [Workforce Management Best Practices](https://www.callcentrehelper.com/)

## 🎓 Citation

If you use this toolkit in academic work, please cite:
```
Call Center Workforce Planning Toolkit
URL: https://github.com/[your-username]/callcenterexample
Year: 2025
```

---

**Built with ❤️ for call center professionals worldwide**

**Last Updated:** November 2025
