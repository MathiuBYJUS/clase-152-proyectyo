from tkinter import * 
root=Tk() 
root.title("Matrices multidimensionales") 
root.geometry("500x500")

label_1=Label(text="Matrizes")
label_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)
label_2=Label(text="")
label_2.place(relx=0.5 , rely=0.6 , anchor=CENTER)
nombres=["James","Jhon","Juan"]
nombres_letras=n_l=[["James","A"],["Jhon","B"],["Juan","C"]]
array_3=array_31=array32=[[["James","A","Bueno"],["Jhon","B","Muy bueno"],["Jose","C","Excelente"]]]

print (nombres[0])
print (nombres_letras[0][1])
print (array_3[0][2][2])

def funcioncilla():
    label_2["text"]="La calificacion del alumno " + nombres[0] + " es " + nombres_letras[0][1] + " porque es un " + array_3[0][2][2] +  " alumno "



button_1=Button(root,text="Daame click", command=funcioncilla,bg="green")
button_1.place(relx=0.5 , rely=0.7, anchor=CENTER)
 



root.mainloop()

