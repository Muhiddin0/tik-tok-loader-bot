
import requests



r = requests.get('https://download.tik-cdn.com/link/1698467230/f85ad86689d341f13b8566b9b735e31c74b6ed62bfcfe1f9c419093b37530745?file=aHR0cHM6Ly9zZjE2LWllcy1tdXNpYy12YS50aWt0b2tjZG4uY29tL29iai90b3MtdXNlYXN0MmEtdmUtMjc3NC9vWTh5TnJianRDVkFCT3hkRHVlWHRaZkJRVnFib05nRXRBZ2dRbj9uYW1lPVRpa1ZpZGVvLkFwcF83Mjk0NzIyMDEzOTUwNjU5ODQyLm1wMw')

def file_name(headers):

    error = headers.get('Content-Type')
    if error == 'text/plain; charset=utf-8':
        return 'error'
    
    text = headers.get('Content-Disposition')

    return text[-4:]

print(file_name(r.headers))