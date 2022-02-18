# pyapod

A PyQt interface of the popular [Astronomy Picture Of the Day](https://apod.nasa.gov/apod/astropix.html) website posting photos & videos of Space everyday since 1995.

![Gui_screenshot](img/screenshot.png)

## How to setup
1. Clone the repo and cd into it
2. Activate your virtual environment
3. install the dependencies : 
    ```
    pip install -r requirements.txt
    ```
4. You need to generate your own [NASA api key](https://api.nasa.gov/)
5. Paste it into `api_key.json` at the root of the repo
    ```
    {
        "api_key": "YOUR_KEY_GOES_THERE"
    }
    ```

## Contributing
* **Report a bug:** See [issues](https://github.com/Foussy/APOD_NASA_Foussy/issues)

## License
[MIT License](LICENSE)
