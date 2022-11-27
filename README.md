# Nudeny Restful API

## Classification
```
POST /classify
```

Curl
```
curl -X 'POST' \
  'http://127.0.0.1:8000/classify/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@uau74uozrrw91.jpg;type=image/jpeg' \
  -F 'files=@uofb0i4t6mw91.jpg;type=image/jpeg'
```

Sample JSON response
```json
{
  "predictions": [
    {
      "uau74uozrrw91.jpg": "nude"
    },
    {
      "uofb0i4t6mw91.jpg": "nude"
    }
  ]
}
```

## Detection
```
POST /draw_bounding_box
```

Curl
```
curl -X 'POST' \
  'http://127.0.0.1:8000/draw_bounding_box/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@99115338_011_190e.jpg;type=image/jpeg' \
  -F 'files=@sv3vtwpccex91.png;type=image/png'
```

Sample JSON response
```json
{
  "predictions": [
    {
      "filename": "99115338_011_190e.jpg",
      "url": "http://127.0.0.1:8000/static/247e2fbc-a9f6-4645-bb20-9a97293c4827-99115338_011_190e.jpg",
      "exposed_parts": {
        "female_genitalia": {
          "confidence_score": 67.99014210700989,
          "top": 337,
          "left": 120,
          "bottom": 388,
          "right": 153
        },
        "female_breast": {
          "confidence_score": 53.750550746917725,
          "top": 162,
          "left": 85,
          "bottom": 229,
          "right": 234
        },
        "buttocks": {
          "confidence_score": 52.793073654174805,
          "top": 388,
          "left": 72,
          "bottom": 433,
          "right": 200
        }
      }
    },
    {
      "filename": "sv3vtwpccex91.png",
      "url": "http://127.0.0.1:8000/static/467d7c9c-8f37-42a4-a88a-6794b0e17fec-sv3vtwpccex91.png",
      "exposed_parts": {
        "male_genitalia": {
          "confidence_score": 91.17953777313232,
          "top": 590,
          "left": 251,
          "bottom": 667,
          "right": 294
        }
      }
    }
  ]
}
```

## Censor

```
POST /censor
```

Curl
```
curl -X 'POST' \
  'http://127.0.0.1:8000/censor/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@99115338_011_190e.jpg;type=image/jpeg' \
  -F 'files=@sv3vtwpccex91.png;type=image/png'
```

Sample JSON response
```json
{
  "predictions": [
    {
      "filename": "99115338_011_190e.jpg",
      "url": "http://127.0.0.1:8000/static/94410a87-c00f-4424-9fda-91cec34910c3-99115338_011_190e.jpg",
      "exposed_parts": {
        "female_genitalia": {
          "confidence_score": 67.99014210700989,
          "top": 337,
          "left": 120,
          "bottom": 388,
          "right": 153
        },
        "female_breast": {
          "confidence_score": 53.750550746917725,
          "top": 162,
          "left": 85,
          "bottom": 229,
          "right": 234
        },
        "buttocks": {
          "confidence_score": 52.793073654174805,
          "top": 388,
          "left": 72,
          "bottom": 433,
          "right": 200
        }
      }
    },
    {
      "filename": "sv3vtwpccex91.png",
      "url": "http://127.0.0.1:8000/static/7d811f62-c3b2-4558-9617-30a69a05823c-sv3vtwpccex91.png",
      "exposed_parts": {
        "male_genitalia": {
          "confidence_score": 91.17953777313232,
          "top": 590,
          "left": 251,
          "bottom": 667,
          "right": 294
        }
      }
    }
  ]
}
```

## Example censored image stored in the static folder.
![me](https://i.imgur.com/wz77v0F.jpeg)
