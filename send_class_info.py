import requests

with open("class_info.csv","rb") as f:
    for line in f.readlines()[1:]:
        line = line.decode()
        line_list = line.split(",")
        time_string = line_list[2]
        line_list[2] = time_string[:4]+"-"+time_string[4:6]+"-"+time_string[6:]
        line_list[3] = line_list[3].strip()
        send_data = {}
        send_data["class_number"],send_data["class_name"],send_data["rx_time"],send_data["yx"] = line_list
        response = requests.post(url="http://127.0.0.1:8000/class_info/",data=send_data)

        print(send_data)
        print(response.json())
