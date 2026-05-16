import subprocess

input_file = "ip_addr.txt"
output_file = "result.txt"

# Открываем входной и выходной файлы:
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        ip = line.strip()
        if not ip:
            continue
# Запуск команды ping:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "1000", ip],
            #stdout = subprocess.DEVNULL,
            #stderr = subprocess.DEVNULL
        )

# Проверка результата:
        if result.returncode == 0:
            status = "UP"
        else:
            status = "DOWN"

# Запись результата в файл
        f_out.write(f"{ip} - {status}\n")
        print(f"{ip} - {status}")