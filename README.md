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
  -F 'files=@uofb0i4t6mw91.jpg;type=image/jpeg'
```

Sample JSON response
```json
{
  "predictions": [
    {
      "filename": "99115338_011_190e.jpg",
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
      "filename": "uofb0i4t6mw91.jpg",
      "exposed_parts": {
        "male_genitalia": {
          "confidence_score": 93.42241287231445,
          "top": 630,
          "left": 275,
          "bottom": 795,
          "right": 346
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
  -F 'files=@uofb0i4t6mw91.jpg;type=image/jpeg'
```

Sample JSON response
```json
{
  "predictions": [
    {
      "filename": "99115338_011_190e.jpg",
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
      "filename": "uofb0i4t6mw91.jpg",
      "exposed_parts": {
        "male_genitalia": {
          "confidence_score": 93.42241287231445,
          "top": 630,
          "left": 275,
          "bottom": 795,
          "right": 346
        }
      }
    }
  ]
}
```

## Example censored image stored in the tmp folder.
![me](https://i.imgur.com/wz77v0F.jpeg)
