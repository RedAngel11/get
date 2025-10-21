import time
from r2r_adc import R2R_ADC
import adc_plot as plot

if __name__ == "__main__":

    duration = 3.0        # продолжительность измерения
    voltage_values = []
    time_values = []    

    try:
        adc = R2R_ADC(range = 3.281, compare_time=0.01, verbose=False)

        start_time = time.time()      
        while True:
            current_time = time.time() - start_time  
            if current_time > duration:
                break

            voltage_values.append(adc.get_sc_voltage())
            time_values.append(current_time)

            time.sleep(0.01)
        
        print(f"Получите-распишитесь. Всего точек: {len(time_values)}")
        
        # Строим графики
        plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage=3.281)
        plot.plot_sampling_period_hist(time_values)

    except KeyboardInterrupt: print("\nТы вырубила прогу")
    finally: adc.deinit()
