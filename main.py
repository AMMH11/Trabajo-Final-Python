from api_client import fetch_stock_data
from database import initialize_db, save_stock_data, get_saved_tickers
from plotter import plot_ticker_data

def main():
    
    initialize_db()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Actualizar datos")
        print("2. Visualizar datos")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ticker = input("Ingrese ticker a pedir: ")
            start_date = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
            end_date = input("Ingrese fecha de fin (YYYY-MM-DD): ")
            print("Pidiendo datos ...")
            data = fetch_stock_data(ticker, start_date, end_date)
            if data:
                save_stock_data(ticker, data)
                print("Datos guardados correctamente.")
            else:
                print("No se pudieron obtener los datos.")

        elif opcion == "2":
            print("\n--- Visualización de Datos ---")
            print("1. Resumen de datos guardados")
            print("2. Graficar un ticker")
            sub_opcion = input("Elige una opción: ")

            if sub_opcion == "1":
                tickers = get_saved_tickers()
                if tickers:
                    print("\nLos tickers guardados en la base de datos son:")
                    for ticker, start, end in tickers:
                        print(f"{ticker} - {start} <-> {end}")
                else:
                    print("No hay datos guardados en la base de datos.")

            elif sub_opcion == "2":
                ticker = input("Ingrese el ticker a graficar: ")
                plot_ticker_data(ticker)

            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()




