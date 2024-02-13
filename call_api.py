import requests

def main():
    api_site_url = "https://speech-text-api.onrender.com"
    api_params = {
        "data_list": [] ,
        "data_str": "" ,
        "data_int": 0 ,
    }
    response = requests.post(api_site_url , json=api_params)
    json_data_from_api = response.json()
    api_output_text = json_data_from_api["api_output_text"]
    print(api_output_text)

if __name__ == "__main__":
    main()