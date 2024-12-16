class Clima:
    def __init__(self, dia, temperatura_maxima, temperatura_minima, precipitacion):
        # Atributos privados (encapsulamiento)
        self.__dia = dia
        self.__temperatura_maxima = temperatura_maxima
        self.__temperatura_minima = temperatura_minima
        self.__precipitacion = precipitacion

    # Métodos para obtener información
    def get_dia(self):
        return self.__dia

    def get_temperatura_maxima(self):
        return self.__temperatura_maxima

    def get_temperatura_minima(self):
        return self.__temperatura_minima

    def get_precipitacion(self):
        return self.__precipitacion

    # Métodos para establecer información
    def set_temperatura_maxima(self, temperatura_maxima):
        self.__temperatura_maxima = temperatura_maxima

    def set_temperatura_minima(self, temperatura_minima):
        self.__temperatura_minima = temperatura_minima

    def set_precipitacion(self, precipitacion):
        self.__precipitacion = precipitacion

    # Método para mostrar datos del clima
    def mostrar_informacion(self):
        return f"Día: {self.__dia}, Máx: {self.__temperatura_maxima}°C, Mín: {self.__temperatura_minima}°C, Precipitación: {self.__precipitacion}mm"

class ClimaSemanal:
    def __init__(self):
        self.__datos_semanales = []  # Lista para almacenar objetos de tipo Clima

    # Método para agregar datos diarios
    def agregar_dia(self, clima):
        if isinstance(clima, Clima):
            self.__datos_semanales.append(clima)
        else:
            raise ValueError("El objeto debe ser de tipo Clima")

    # Método para calcular el promedio semanal
    def calcular_promedios(self):
        total_maxima = 0
        total_minima = 0
        total_precipitacion = 0
        dias = len(self.__datos_semanales)

        for clima in self.__datos_semanales:
            total_maxima += clima.get_temperatura_maxima()
            total_minima += clima.get_temperatura_minima()
            total_precipitacion += clima.get_precipitacion()

        if dias == 0:
            return "No hay datos para calcular promedios"

        return {
            "promedio_maxima": total_maxima / dias,
            "promedio_minima": total_minima / dias,
            "promedio_precipitacion": total_precipitacion / dias
        }

    # Método para mostrar la información semanal
    def mostrar_resumen(self):
        for clima in self.__datos_semanales:
            print(clima.mostrar_informacion())

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de ClimaSemanal
    semana = ClimaSemanal()

    # Agregar información diaria del clima
    semana.agregar_dia(Clima("Lunes", 35, 25, 6))
    semana.agregar_dia(Clima("Martes", 31, 21, 1))
    semana.agregar_dia(Clima("Miércoles", 38, 26, 11))
    semana.agregar_dia(Clima("Jueves", 30, 22, 4))
    semana.agregar_dia(Clima("Viernes", 28, 19, 3))
    semana.agregar_dia(Clima("Sábado", 25, 15, 1))
    semana.agregar_dia(Clima("Domingo", 28, 18, 3))

    # Mostrar resumen de datos diarios
    print("Resumen semanal:")
    semana.mostrar_resumen()

    # Calcular promedios semanales
    promedios = semana.calcular_promedios()
    print("\nPromedios semanales:")
    print(f"Temperatura máxima promedio: {promedios['promedio_maxima']:.2f}°C")
    print(f"Temperatura mínima promedio: {promedios['promedio_minima']:.2f}°C")
    print(f"Precipitación promedio: {promedios['promedio_precipitacion']:.2f}mm")

