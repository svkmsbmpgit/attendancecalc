AMT = int(input("Enter Attendance in AMT: "))
BEX = int(input("Enter Attendance in BEX: "))
CWP = int(input("Enter Attendance in CWP: "))
EVS = int(input("Enter Attendance in EVS: "))
FCN = int(input("Enter Attendance in FCN: "))
FSL = int(input("Enter Attendance in FSL: "))
PRC = int(input("Enter Attendance in PRC: "))

AMTt = 75
BEXt = 56
CWPt = 28
EVSt = 30
FCNt = 75
FSLt = 89
PRCt = 84

AMTp = (100 * AMT) / AMTt
BEXp = (100 * BEX) / BEXt
CWPp = (100 * CWP) / CWPt
EVSp = (100 * EVS) / EVSt
FCNp = (100 * FCN) / FCNt
FSLp = (100 * FSL) / FSLt
PRCp = (100 * PRC) / PRCt

# Calculate the number of lectures needed to reach 80% attendance
AMTl = ((80 * AMTt) / 100) - AMT
BEXl = ((80 * BEXt) / 100) - BEX
CWPl = ((80 * CWPt) / 100) - CWP
EVSl = ((80 * EVSt) / 100) - EVS
FCNl = ((80 * FCNt) / 100) - FCN
FSLl = ((80 * FSLt) / 100) - FSL
PRCl = ((80 * PRCt) / 100) - PRC

# Check and print results for each subject
if AMTp < 80:
    print(f"Attendance is Less than Needed in AMT: {AMTp}%")
    print(f"You need to attend {AMTl} more lectures.")
else:
    print("Attendance is good in AMT")

if BEXp < 80:
    print(f"Attendance is Less than Needed in BEX: {BEXp}%")
    print(f"You need to attend {BEXl} more lectures.")
else:
    print("Attendance is good in BEX")

if CWPp < 80:
    print(f"Attendance is Less than Needed in CWP: {CWPp}%")
    print(f"You need to attend {CWPl} more lectures.")
else:
    print("Attendance is good in CWP")

if EVSp < 80:
    print(f"Attendance is Less than Needed in EVS: {EVSp}%")
    print(f"You need to attend {EVSl} more lectures.")
else:
    print("Attendance is good in EVS")

if FCNp < 80:
    print(f"Attendance is Less than Needed in FCN: {FCNp}%")
    print(f"You need to attend {FCNl} more lectures.")
else:
    print("Attendance is good in FCN")

if FSLp < 80:
    print(f"Attendance is Less than Needed in FSL: {FSLp}%")
    print(f"You need to attend {FSLl} more lectures.")
else:
    print("Attendance is good in FSL")

if PRCp < 80:
    print(f"Attendance is Less than Needed in PRC: {PRCp}%")
    print(f"You need to attend {PRCl} more lectures.")
else:
    print("Attendance is good in PRC")

GrossA = ((AMT + BEX + CWP + EVS + FCN + FSL + PRC)/(AMTt + BEXt + CWPt + EVSt + FCNt + FSLt + PRCt)) * 100

print(f"Gross Attendance is {GrossA}")


print("""TIME TABLE: 
            MON TUE WED THU FRI SAT
      AMT   1       1           3
      BEX   3           1   1
      CWP   2
      EVS               1   1
      FCN   1   1   3           1
      FSL       2       3       1
      PRC       2           4


      """)
 
 
