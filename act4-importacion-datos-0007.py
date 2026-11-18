import pandas as pd
import matplotlib.pyplot as plt
# Alexandro Aguilar NC 0007
print("+-+-+ 1. Crear un diccionario con diez listas y seis elementos por lista. +-+-+")
pacientes_clinica = {
    'id_paciente': [1001, 1002, 1003, 1004, 1005, 1006],
    'nombre': ['Laura', 'Pedro', 'Sofia', 'Miguel', 'Elena', 'Jorge'],
    'edad': [34, 45, 28, 62, 19, 51],
    'tipo_sangre': ['O+', 'A-', 'B+', 'AB+', 'O-', 'A+'],
    'peso_kg': [65.5, 78.2, 58.0, 85.1, 52.3, 74.0],
    'altura_cm': [165, 175, 160, 180, 155, 172],
    'diagnostico': ['Gripe', 'Hipertension', 'Migraña', 'Diabetes', 'Alergia', 'Gastritis'],
    'dias_hospitalizacion': [0, 3, 0, 5, 1, 2],
    'medicamento': ['Paracetamol', 'Enalapril', 'Ibuprofeno', 'Metformina', 'Loratadina', 'Omeprazol'],
    'proximo_control': ['2024-02-01', '2024-01-15', '2024-03-10', '2024-01-20', '2024-04-05', '2024-02-28']
}
print("Analisis exploratorio de datos")
print("EDA (Exploratory Data Analysis) por Alexandro Aguilar 0007")

print("+-+-+ 2. Convertir el diccionario en un DataFrame. +-+-+")
df = pd.DataFrame(pacientes_clinica)
print("\n--- TABLA ORIGINAL DE PACIENTES ---")
print(df)

print("+-+-+ Convertir el Data Frame en archivo CSV +-+-+")
df.to_csv(
    'pacientes_clinica_0007.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("+-+-+ 8. Leer los datos desde el archivo CSV +-+-+")
print("pacientes_clinica_0007.csv")

df = pd.read_csv('pacientes_clinica_0007.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("+-+-+ 🔍 9. Análisis Exploratorio de Datos (EDA) +-+-+")
# 5. Primeros y últimos registros
print("+-+-+ \n1. PRIMEROS REGISTROS (Head): +-+-+ ")
print(df.head(3)) # Muestra los primeros 3

print("+-+-+ \n2. ÚLTIMOS REGISTROS (Tail): +-+-+")
print(df.tail(2)) # Muestra los últimos 2

print("+-+-+ 6. Dimensiones y estructura +-+-+")
print(df) # mostrar tabla o matriz original
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()
# 7. Estadísticas y limpieza
print("\n +-+-+-+-+-+-+-+ 7. ESTADÍSTICAS DESCRIPTIVAS: +-+-+-+-+-+-+-+")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Diagnostico:", df['diagnostico'].unique())
# 8. Análisis específico
print(df)
print(" ---------------------------------------------------------------------- ")
print("\n11. PACIENTES POR TIPO DE SANGRE:")
print(df['tipo_sangre'].value_counts())
print("\n12. PROMEDIO DE EDAD:", round(df['edad'].mean(), 2), "años")
print("13. EDAD MÁXIMA:", df['edad'].max(), "años")
print("14. EDAD MÍNIMA:", df['edad'].min(), "años")

# 9. Ordenamiento, filtrado y agrupación
print("\n9. Ordenamiento, filtrado y agrupación")
print("\n +-+-+-+ 15. PACIENTES ORDENADOS POR EDAD (Mayor a menor): +-+-+-+")
print(df.sort_values(by='edad', ascending=False))

print("\n16. PACIENTES CON EDAD MAYOR A 40 AÑOS:")
filtro = df[df['edad'] > 40]
print(filtro)

print("\n17. RESUMEN POR TIPO DE SANGRE:")
resumen = df.groupby('tipo_sangre').agg(
    pacientes=('id_paciente', 'count'),
    edad_promedio=('edad', 'mean'),
    edad_maxima=('edad', 'max')
)
print(resumen)
# 18. Gráfica de barras: Pacientes por tipo de sangre
print("18. Gráfica de barras: Pacientes por tipo de sangre")
conteo = df['tipo_sangre'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Pacientes por tipo de sangre Alexandro Aguilar NC 0007')
plt.xlabel('Tipo de sangre')
plt.ylabel('Cantidad de pacientes')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 19. Gráfica de barras: Peso por paciente
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['peso_kg'], color='lightgreen')
plt.title('Peso por paciente EDA por Alexandro 0007')
plt.xlabel('Paciente')
plt.ylabel('Peso (kg)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de edades
plt.figure(figsize=(8, 5))
plt.hist(df['edad'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de edades de pacientes EDA Alexandro 0007')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Edad vs Peso
plt.figure(figsize=(8, 5))
plt.scatter(df['edad'], df['peso_kg'], color='red', s=100)
plt.title('Relación entre edad y peso EDA por Alexandro 0007')
plt.xlabel('Edad')
plt.ylabel('Peso (kg)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de pesos
plt.figure(figsize=(7, 5))
plt.boxplot(df['peso_kg'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de pesos (Boxplot) EDA Alexandro 0007')
plt.ylabel('Peso (kg)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Alexandro 0007')
plt.tight_layout()
plt.show()
# Alexandro Aguilar NC 0007



