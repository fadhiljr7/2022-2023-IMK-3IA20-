#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN/bin/activate..

import streamlit as st

# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)

# st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("logolabti.png", width=150)

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: white;'>Information Technology Laboratory</h1>", unsafe_allow_html=True)

st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.markdown("""
<!-- Image and text -->
<nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #BA3EC8">
  <a class="navbar-brand" href="#">
    University of Gunadarma
  </a>
</nav>
""", unsafe_allow_html=True)

st.write("""
# **Final Score IMK 3IA20**
Keep fighting and never surrender. #ThisIsOnlyTheBegining
""")

npm = st.text_input("NPM : ")
search = st.button("Search")

if search or npm:
    if npm == "50420055":
        pretest = (680)/7
        posttest = (700)/7
        activity = (620)/7
        fnlrpt = (460)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: AFDHALUL ICHSAN YOURDAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "12345678":
        pretest = (95+90+80+60+50+90+90+70)/7
        posttest = (95+90+80+50+95+90+20+70)/7
        activity = (20+70+70+70+70+90+20+70)/7
        fnlrpt = (20+70+70+70+70+90+100+70)/7
        exscore = 78
        attdnc = (7/8)*100
        st.write("Name: CONTOH INPUT")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)
    
    elif npm == "50420058":
        pretest = (700)/7
        posttest = (700)/7
        activity = (480)/7
        fnlrpt = (170)/7
        exscore = 0
        attdnc = (7/7)*100
        st.write("Name: AFIF HANUBHOWO PRIHATMORO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420080":
        pretest = (680)/7
        posttest = (700)/7
        activity = (670)/7
        fnlrpt = (645)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: AHMAD MUHAMAD SALIM ALHADAR")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420150":
        pretest = (680)/7
        posttest = (700)/7
        activity = (620)/7
        fnlrpt = (575)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: ALVIAN DHARMAWAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420155":
        pretest = (680)/7
        posttest = (700)/7
        activity = (580)/7
        fnlrpt = (625)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: ALYA KHALISHA MACHFUD")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 3")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420173":
        pretest = (0)/7
        posttest = (0)/7
        activity = (0)/7
        fnlrpt = (0)/7
        exscore = 0
        attdnc = (0/7)*100
        st.write("Name: ANDI ALVIAN PRASETIO")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/2/3/4/5/6/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420226":
        pretest = (700)/7
        posttest = (700)/7
        activity = (650)/7
        fnlrpt = (240)/7
        exscore = 98
        attdnc = (7/7)*100
        st.write("Name: Arika Mulyanti")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420229":
        pretest = (600)/7
        posttest = (600)/7
        activity = (640)/7
        fnlrpt = (510)/7
        exscore = 93
        attdnc = (7/7)*100
        st.write("Name: ARIQ NAUFAL FADHLURRAHMAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420242":
        pretest = (620)/7
        posttest = (700)/7
        activity = (530)/7
        fnlrpt = (80)/7
        exscore = 78
        attdnc = (3/7)*100
        st.write("Name: ARYA RAUFAL HAMDALA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 2/4/5/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420274":
        pretest = (620)/7
        posttest = (660)/7
        activity = (670)/7
        fnlrpt = (520)/7
        exscore = 94
        attdnc = (7/7)*100
        st.write("Name: BAHA WILLIAMS AZAEL")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420291":
        pretest = (0)/7
        posttest = (0)/7
        activity = (0)/7
        fnlrpt = (0)/7
        exscore = 0
        attdnc = (0/7)*100
        st.write("Name: BINTANG SAEKAPUTRA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/2/3/4/5/6/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420418":
        pretest = (460)/7
        posttest = (460)/7
        activity = (130)/7
        fnlrpt = (340)/7
        exscore = 80
        attdnc = (2/7)*100
        st.write("Name: BINTARA SATRIA NUGROHO")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/2/3/4/5")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420391":
        pretest = (380)/7
        posttest = (380)/7
        activity = (200)/7
        fnlrpt = (150)/7
        exscore = 0
        attdnc = (5/7)*100
        st.write("Name: DITO RIYANTO RAMADHAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 2/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420453":
        pretest = (700)/7
        posttest = (700)/7
        activity = (600)/7
        fnlrpt = (500)/7
        exscore = 92
        attdnc = (7/7)*100
        st.write("Name: FALDY ARGADITYA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420501":
        pretest = (380)/7
        posttest = (480)/7
        activity = (290)/7
        fnlrpt = (150)/7
        exscore = 78
        attdnc = (6/7)*100
        st.write("Name: FITRAH RAMADHANI")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420539":
        pretest = (700)/7
        posttest = (680)/7
        activity = (490)/7
        fnlrpt = (228)/7
        exscore = 80
        attdnc = (6/7)*100
        st.write("Name: HANIF MUSTAJAB")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420545":
        pretest = (680)/7
        posttest = (700)/7
        activity = (600)/7
        fnlrpt = (100)/7
        exscore = 95
        attdnc = (7/7)*100
        st.write("Name: HARYO PUTRO SETYANTO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420550":
        pretest = (680)/7
        posttest = (700)/7
        activity = (630)/7
        fnlrpt = (500)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: HERMANIA SAFITRI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420727":
        pretest = (660)/7
        posttest = (700)/7
        activity = (620)/7
        fnlrpt = (580)/7
        exscore = 85
        attdnc = (7/7)*100
        st.write("Name: MOCHAMMAD PUTRA DINA RISDIANTO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420760":
        pretest = (700)/7
        posttest = (700)/7
        activity = (550)/7
        fnlrpt = (510)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: MUHAMAD JAVIER ZAMZUFAR")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420767":
        pretest = (540)/7
        posttest = (580)/7
        activity = (480)/7
        fnlrpt = (240)/7
        exscore = 78
        attdnc = (3/7)*100
        st.write("Name: MUHAMAD RIZAL FANDIKA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 2/4/5/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420798":
        pretest = (680)/7
        posttest = (700)/7
        activity = (600)/7
        fnlrpt = (560)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: MUHAMMAD ASAD RAMADHAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420352":
        pretest = (700)/7
        posttest = (680)/7
        activity = (570)/7
        fnlrpt = (570)/7
        exscore = 84
        attdnc = (6/7)*100
        st.write("Name: MUHAMMAD AVIF ROHMADIAWAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50420900":
        pretest = (600)/7
        posttest = (680)/7
        activity = (410)/7
        fnlrpt = (470)/7
        exscore = 100
        attdnc = (5/7)*100
        st.write("Name: MUHAMMAD REZA HIDAYAT")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 5/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420401":
        pretest = (700)/7
        posttest = (680)/7
        activity = (560)/7
        fnlrpt = (520)/7
        exscore = 92
        attdnc = (7/7)*100
        st.write("Name: NANDI RIFALDI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420004":
        pretest = (600)/7
        posttest = (600)/7
        activity = (560)/7
        fnlrpt = (155)/7
        exscore = 0
        attdnc = (6/7)*100
        st.write("Name: PETRA EUAGGELION DEVON")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420007":
        pretest = (0)/7
        posttest = (0)/7
        activity = (0)/7
        fnlrpt = (0)/7
        exscore = 0
        attdnc = (0/7)*100
        st.write("Name: PRAMUDYA REIHANSYAH SUNDAFA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/2/3/4/5/6/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420011":
        pretest = (700)/7
        posttest = (700)/7
        activity = (650)/7
        fnlrpt = (610)/7
        exscore = 95
        attdnc = (7/7)*100
        st.write("Name: PRAYOGA DANUARTA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420051":
        pretest = (700)/7
        posttest = (700)/7
        activity = (570)/7
        fnlrpt = (400)/7
        exscore = 100
        attdnc = (6/7)*100
        st.write("Name: RALFATIHANUR ZIAFIQ MAKPAL")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420162":
        pretest = (700)/7
        posttest = (700)/7
        activity = (580)/7
        fnlrpt = (480)/7
        exscore = 95
        attdnc = (7/7)*100
        st.write("Name: SALSABILA FEBRIYANA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420219":
        pretest = (540)/7
        posttest = (500)/7
        activity = (150)/7
        fnlrpt = (300)/7
        exscore = 80
        attdnc = (0/7)*100
        st.write("Name: SYAFIQ SHAFWAN FAUZAN")
        st.write("Attendance: %.0f" % attdnc, "% 1/2/3/4/5/6/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420289":
        pretest = (680)/7
        posttest = (700)/7
        activity = (150)/7
        fnlrpt = (150)/7
        exscore = 78
        attdnc = (0/7)*100
        st.write("Name: YAZID FARHAN MUZAKKY")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/2/3/4/5/6/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420299":
        pretest = (660)/7
        posttest = (700)/7
        activity = (600)/7
        fnlrpt = (550)/7
        exscore = 92
        attdnc = (7/7)*100
        st.write("Name: YONATHAN CHRISTIANTO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421466":
        pretest = (800)/7
        posttest = (800)/7
        activity = (740)/7
        fnlrpt = (640)/7
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: TEGAR DWI SEPTIADI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421552":
        pretest = (800)/7
        posttest = (780)/7
        activity = (640)/7
        fnlrpt = (640)/7
        exscore = 90
        attdnc = (8/8)*100
        st.write("Name: ZAHIDAN ARDHIANSYAH")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    else:
        st.write("NPM not found")

    estgrade = (pretest+posttest+activity+fnlrpt+exscore)/5
    if estgrade >= 80:
        st.write("Estimation grade from LAB TI: A")
    elif estgrade >= 70:
        st.write("Estimation grade from LAB TI: B")
    elif estgrade >= 60:
        st.write("Estimation grade from LAB TI: C")
    else:
        st.write("Estimation grade from LAB TI: D")
    st.balloons()

#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN/bin/activate
