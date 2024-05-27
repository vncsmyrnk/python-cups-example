![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Python Cups Example

This example uses flask and pycups for creating a web server that prints files.

## Run with Docker

```bash
docker build -t example-cups-api
docker run --rm -it -p 5000:5000 example-cups-api
```

## Examples

```bash
curl -X GET localhost:5000/printers-info
```

```json
{
   "hp-casa":{
      "device-uri":"ipp://192.168.X.Y/ipp/print",
      "printer-info":"hp-casa",
      "printer-is-shared":true,
      "printer-location":"",
      "printer-make-and-model":"HP LaserJet Professional - IPP Everywhere",
      "printer-state":3,
      "printer-state-message":"",
      "printer-state-reasons":[
         "cups-ipp-conformance-failure-report",
         "cups-ipp-missing-send-document"
      ],
      "printer-type":4100,
      "printer-uri-supported":"ipp://localhost/printers/hp-casa"
   }
}
```

---

```bash
curl -X GET 192.168.100.7:5000/print-file
```

Output:

```json
{
   "job_id":2
}
```
