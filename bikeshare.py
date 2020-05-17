#Inicio

#Librerias

import numpy as np
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import time
import multiprocessing
from datetime import timedelta

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# PARA HACER: obtenga la entrada del usuario para la ciudad (Chicago, Nueva York, Washington). SUGERENCIA: Use un ciclo while para manejar entradas inválidas

# TO DO: get user input for month (all, january, february, ... , june)
# PARA HACER: obtenga la entrada del usuario para el mes (todos, enero, febrero, ..., junio)

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
# PARA HACER: obtenga la entrada del usuario para el día de la semana (todos, lunes, martes, ... domingo)

Ciudades =['Chicago','New York', 'Washington']
Dias_Semana= {'Lunes': 'Monday','Martes':'Tuesday','Miercoles':'Wednesday','Jueves':'Thursday','Viernes':'Friday','Sabado':'Saturday','Domingo':'Sunday'}
mensajes =['A continuación vamos a vizualizar los de datos de '+Ciudades[0],'A continuación vamos a vizualizar los de datos de '+Ciudades[1], 'A continuación vamos a vizualizar los de datos de '+Ciudades[2], 'EN el momento No tenemos datos para su ciudad ¿Por qué no intenta con: New York, Chicago o Washington?']
ciudad=""
Resultado=""
week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
search_city = input('Bienvenido a las estadisticas de Bikeshare desglosada por Ciudad, Mes y Dia, Por favor ingrese su ciudad: ')
ciudad = search_city.lower()
while search_city.lower() == "chicago" or "new york" or "washington":
    if search_city.lower() == "chicago":
      Resultado  = (mensajes[0])
    elif search_city.lower() == "new york":
      Resultado  = (mensajes[1])
    elif search_city.lower() == "washington":
      Resultado  = (mensajes[2])
    else:
      Resultado  =(mensajes[3])
      print(ciudad)
      print(Resultado)
      search_city = input('Ingrese su ciudad ')  
    break
    if search_city == "chicago":
      Resultado = (mensajes[0])
    elif search_city == "new york":
      Resultado = (mensajes[1])
    elif search_city == "washington":
      Resultado = (mensajes[2])
    break

print(Resultado)
     
ciudad = search_city.lower()
Input_Fecha = input('Por favor ingrese el primer mes del semestre de 2017: ')
month = Input_Fecha.lower()

Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
df = pd.read_csv(Datos_Ciudades[ciudad])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['dia_semana'] = df['Start Time'].dt.day_name()
df['month'] = df['Start Time'].dt.month
if month != 'all':
  months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
  month = months.index(month) + 1
  df = df[df['month'] == month]
Dias_Semana= {'Lunes': 'Monday','Martes':'Tuesday','Miercoles':'Wednesday','Jueves':'Thursday','Viernes':'Friday','Sabado':'Saturday','Domingo':'Sunday'}
Input_day = input('Por favor ingrese el día de la semana el cuál quisiera ver: ')
day_es=Input_day.capitalize()

if Dias_Semana[day_es] != 'all':
   df = df[df['dia_semana'] == Dias_Semana[day_es]]

# TO DO: display the most common month
# PARA HACER: muestra el mes más común

# TO DO: display the most common day of week
# PARA HACER: muestra el día más común de la semana

# TO DO: display the most common start hour
# PARA HACER: muestra la hora de inicio más común

# Se vuelve a cargar la información ya que si de deja filtrada únicamente traera el mes filtrado en lugar del mes más común, al igual que la hora y el dia, por lo anterior no correspondería a la pregunta efectuada.

Estadistica_Meses = input('¿Desearía ver las cifras de las estadisticas de los meses?: ')
if Estadistica_Meses == 'si' or Estadistica_Meses == 'Si' or Estadistica_Meses == 'SI':
  Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
  df = pd.read_csv(Datos_Ciudades[ciudad])  
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df['month'] = df['Start Time'].dt.month
  df['day'] = df['Start Time'].dt.dayofweek
  df['hour'] = df['Start Time'].dt.hour
  month= df['month'].mode()[0]
  pop_mont = months[month - 1]
  popday= df['Start Time'].dt.dayofweek.mode()[0]
  pop_day = week[popday]
  pophour =df['hour'] = df['Start Time'].dt.hour.mode()[0]
  pop_hour= str(pophour)
  print('El mes más común en '+ciudad+' es '+pop_mont)
  print('El día más común en '+ciudad+' es '+pop_day)
  print('La hora más común en '+ciudad+' es '+pop_hour+':00')

else:

# TO DO: display most commonly used start station
# PARA HACER: muestra la estación de inicio más utilizada

# TO DO: display most commonly used end station
# PARA HACER: muestra la estación final más utilizada

# TO DO: display most frequent combination of start station and end station trip
# PARA HACER: muestra la combinación más frecuente de la estación de inicio y el viaje de la estación final

  Estadistica_Estaciones = input('¿Quiere ver los datos de las estadisticas de las estaciones?: ')
  if Estadistica_Estaciones == 'si' or Estadistica_Estaciones == 'Si' or Estadistica_Estaciones == 'SI':
    month = Input_Fecha.lower()
    Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
    df = pd.read_csv(Datos_Ciudades[ciudad])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['dia_semana'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
      months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
      month = months.index(month) + 1
      df = df[df['month'] == month]
      Dias_Semana= {'Lunes': 'Monday','Martes':'Tuesday','Miercoles':'Wednesday','Jueves':'Thursday','Viernes':'Friday','Sabado':'Saturday','Domingo':'Sunday'}
    if Dias_Semana[day_es] != 'all':
      df = df[df['dia_semana'] == Dias_Semana[day_es]]
      Start_Station=df['Start Station'].mode()[0]
      End_Station=df['End Station'].mode()[0]
      df['Comb_Station'] ='De '+df['Start Station']+' a '+df['End Station']
      Comb_Station = df['Comb_Station'].mode()[0]
      print('La estación de inicio más utilizada es: '+Start_Station)
      print('La estación final más utilizada es: '+End_Station)
      print('La combinación más frecuente de la estación de inicio y el viaje de la estación final es: '+Comb_Station)

# TO DO: display total travel time
# PARA HACER: muestra el tiempo total de viaje

# TO DO: display mean travel time
# PARA HACER: muestra el tiempo medio de viaje

  else:
    Estadistica_viajes = input('¿Quiere ver los datos de las estadisticas de los viajes?: ')
    if Estadistica_viajes == 'si' or Estadistica_viajes == 'Si' or Estadistica_viajes == 'SI':
      month = Input_Fecha.lower()
      Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
      df = pd.read_csv(Datos_Ciudades[ciudad])
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      df['End Time'] = pd.to_datetime(df['End Time'])
      df['dia_semana'] = df['Start Time'].dt.day_name()
      df['month'] = df['Start Time'].dt.month
      if month != 'all':
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        day_es=Input_day.capitalize()
      if Dias_Semana[day_es] != 'all':
        df = df[df['dia_semana'] == Dias_Semana[day_es]]  
        df['duracion'] = df['End Time'] - df['Start Time']
        Viaje_total=df['duracion'].sum()
        Promedio_viaje=df['duracion'].mean()
        print('El promedio de duración de viajes es: '+str(Promedio_viaje))
        print('El total de duración de los viajes es: '+str(Viaje_total))

# TO DO: Display counts of user types
# PARA HACER: muestra recuentos de tipos de usuarios

# TO DO: Display counts of gender
# PARA HACER: muestra los recuentos de género

    else:
      Estadistica_generos = input('¿Qusiera visualizar los datos de las estadisticas de los usuarios?: ')
      if Estadistica_generos == 'si' or Estadistica_generos == 'Si' or Estadistica_generos == 'SI':
        month = Input_Fecha.lower()
        Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
        df = pd.read_csv(Datos_Ciudades[ciudad])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['dia_semana'] = df['Start Time'].dt.day_name()
        df['month'] = df['Start Time'].dt.month
        if month != 'all':
          month = Input_Fecha.lower()
          months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
          month = months.index(month) + 1
          df = df[df['month'] == month]
 
         
        if Dias_Semana[day_es] != 'all':
          day_es=Input_day.capitalize()
          df = df[df['dia_semana'] == Dias_Semana[day_es]]  
          Suma_Tipos = df['User Type'].value_counts()
          Suma_Generos = df['Gender'].value_counts()
          print('Recuento por tipo de usuarios: ')    
          print(Suma_Tipos)
          print('rECUENTO Por tipo de generos: ')    
          print(Suma_Generos)

# TO DO: Display earliest, most recent, and most common year of birth
# PARA HACER: muestra el año de nacimiento más temprano, más reciente y más común

      else:
        Estadistica_nacimientos = input('¿Quiere ver los datos de las estadisticas de las fechas de nacimiento?')
        if Estadistica_nacimientos == 'si' or Estadistica_nacimientos == 'Si' or Estadistica_nacimientos == 'SI':
          Datos_Ciudades = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
          df = pd.read_csv(Datos_Ciudades[ciudad])
          month = Input_Fecha.lower()
          df['Start Time'] = pd.to_datetime(df['Start Time'])
          df['dia_semana'] = df['Start Time'].dt.day_name()
          df['month'] = df['Start Time'].dt.month
          if month != 'all':
            month = Input_Fecha.lower()
            months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
            month = months.index(month) + 1
            df = df[df['month'] == month]
          if Dias_Semana[day_es] != 'all':
            day_es=Input_day.capitalize()
            primer_nacimiento = df['Birth Year'].min()
            ultimo_nacimiento= df['Birth Year'].max()
            moda_nacimientos=df['Birth Year'].mode()[0]
            print('La persona con el año más temprano es: '+str(primer_nacimiento)[0:4])
            print('La persona con el año de nacimiento más reciente: '+str(ultimo_nacimiento)[0:4])
            print('El año de nacimiento más común es: '+str(moda_nacimientos)[0:4])
            print("Muchas Gracias por visitarnos, lo esperamos pronto!")
        else:
            print("Muchas Gracias por visitarnos, lo esperamos pronto!")
            

#Display contents of the CSV file to the display as requested by the user.
# Visualice el contenido del archivo CSV en la pantalla según lo solicite el usuario.
            
def muestra_data_cruda(df):
              inicio_loc = 0
              fin_loc = 5
              data_cruda = input("¿Quiere ver la data cruda?: ").lower()
              if data_cruda  == 'si':
                while fin_loc <= df.shape[0] - 1:
                  print(df.iloc[inicio_loc:fin_loc,:])
                  inicio_loc += 5
                  fin_loc += 5
                  mensaje_final = input("¿Desea continuar?: ").lower()
                  if mensaje_final == 'no':
                 
                    break
                                      
muestra_data_cruda(df)
print("Muchas Gracias por visitarnos, lo esperamos pronto!")