from tkinter import *
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.metrics import cohen_kappa_score

data = pd.read_csv(r"C:\Users\Hp\Desktop\Breast_cancer_data.csv")

x = data.iloc[:, 0:5].values
y = data.iloc[:, 5:6].values

arayuz = Tk()
canvas = Canvas(arayuz, height=600, width=600)
canvas.pack()

frame_top = Frame(arayuz, bg='#FF7F50')
frame_top.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.1)
frame_under = Frame(arayuz, bg='#FF6347')
frame_under.place(relx=0.1, rely=0.13, relwidth=0.8, relheight=0.8)

Head_title = Label(frame_top, bg='#FF7F50', text="Meme Kanseri Teşhisi", font= 'Helvetica 15 ')
Head_title.pack(pady=15)

label1= Label(frame_under, bg='#FF6347',text="mean_radius")
label1.place(relx=0.05, rely=0.08)
box1 = Text(frame_under, height=1,width=20)
box1.place(relx=0.35, rely=0.09)
label2 = Label(frame_under, bg='#FF6347', text="mean_texture")
label2.place(relx=0.05, rely=0.14)
box2 = Text(frame_under, height=1, width=20)
box2.place(relx=0.35, rely=0.15)
label3 = Label(frame_under, bg='#FF6347', text="mean_perimeter")
label3.place(relx=0.05, rely=0.2)
box3 = Text(frame_under, height=1, width=20)
box3.place(relx=0.35, rely=0.21)
label4 = Label(frame_under, bg='#FF6347', text="mean_area")
label4.place(relx=0.05, rely=0.26)
box4 = Text(frame_under, height=1, width=20)
box4.place(relx=0.35, rely=0.27)
label5 = Label(frame_under, bg='#FF6347',text="mean_smoothness")
label5.place(relx=0.05, rely=0.32)
box5 = Text(frame_under, height=1, width=20)
box5.place(relx=0.35, rely=0.33)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=None,
                           n_neighbors=3, p=2, weights='uniform')
knc.fit(x_train, y_train)  # modeli eğitiyoruz.
prediction = knc.predict(x_test)

from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=2, random_state=0)
k_means.fit(x_train,y_train)
km_prediction =k_means.predict(x_test)

var=IntVar()
R1 = Radiobutton(frame_under,text="Knn",variable =var,value=1)
R1.place(relx=0.77, rely=0.18)

R1 = Radiobutton(frame_under,text="Kmeans",variable =var,value=2)
R1.place(relx=0.77, rely=0.25)



def gonder():
    veri1 = float(box1.get("1.0", "end"))
    veri2 = float(box2.get("1.0", "end"))
    veri3 = float(box3.get("1.0", "end"))
    veri4 = float(box4.get("1.0", "end"))
    veri5 = float(box5.get("1.0", "end"))
    cikti = knc.predict([[veri1, veri2, veri3, veri4, veri5]])
    kcikti = k_means.predict(([[veri1, veri2, veri3, veri4, veri5]]))
    if cikti == 1 and kcikti==1:
        cikti = "POZITIF"
        kcikti ="POZITIF"
    else:
        cikti = "NEGATIF"
        kcikti="NEGATIF"

    my_string_var=StringVar()
    acsorestring=StringVar()
    confmatr=StringVar()
    rmse=StringVar()
    kappa=StringVar()

    Sonuc = Label(frame_under, textvariable=my_string_var, bg='#FF6347', height=2, width=40, anchor="w").place(relx=0.01, rely=0.55)
    Acscore = Label(frame_under, textvariable=acsorestring, bg='#FF6347', height=2, width=40,anchor="w").place(relx=0.01, rely=0.61)
    Confusion_matrix = Label(frame_under, textvariable=confmatr, bg='#FF6347', height=2,width=40, anchor="w").place(relx=0.01, rely=0.67)
    msquarederror = Label(frame_under, textvariable=rmse, bg='#FF6347', height=2,width=40, anchor="w").place(relx=0.01, rely=0.75)
    kappa_score = Label(frame_under, textvariable=kappa, bg='#FF6347', height=2, width=40, anchor="w").place(relx=0.01,rely=0.80)

    if var.get():
        if var.get()==1:

            acscore = accuracy_score(y_test, prediction)
            confmat = confusion_matrix(y_test, prediction)
            mserror = mean_squared_error(y_test, prediction)
            kappas = cohen_kappa_score(y_test,prediction)

            my_string_var.set("SONUÇ:   " + cikti)
            acsorestring.set("Accuary Score:   "+str(acscore))
            confmatr.set("Confusion Matrix:   " + str(confmat))
            rmse.set("RMSE:   " + str(mserror))
            kappa.set("KAPPA SCORE:   "+str(kappas))



        elif var.get()==2:

            acscore = accuracy_score(y_test, km_prediction)
            confmat = confusion_matrix(y_test, km_prediction)
            mserror = mean_squared_error(y_test, km_prediction)
            kappas = cohen_kappa_score(y_test, km_prediction)

            my_string_var.set("SONUÇ:   " + str(kcikti))
            acsorestring.set("Accuary Score:   " + str(acscore))
            confmatr.set("Confusion Matrix:   " + str(confmat))
            rmse.set("RMSE:   " + str(mserror))
            kappa.set("KAPPA SCORE:   " + str(kappas))




gonder_butonu = Button(frame_under, text = "Gonder", command = gonder)
gonder_butonu.place(relx=0.45, rely=0.40)
label6 = Label(frame_under, bg='#FF6347', text="Başarım İstatistikleri", font= 'Helvetica 15 underline')
label6.place(relx=0.32, rely=0.47)


arayuz.mainloop()