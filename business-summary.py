import sys

if len(sys.argv) == 5:
    shopname = sys.argv[1]
    ownername = sys.argv[2]
    GST = float(sys.argv[3])
    totalsales = float(sys.argv[4])

else:
    print("No inputs given... using default values")

    shopname = "Kiran Shop"
    ownername = "Kishore"
    GST = 5.0
    totalsales = 10000

    print("\n--- Business Summary (Default) ---")
    print("Shop Name     :\n", shopname)
    print("Owner Name    :\n", ownername)
    print("GST (%)       :\n", GST)
    print("Total Sales   :\n", totalsales)
