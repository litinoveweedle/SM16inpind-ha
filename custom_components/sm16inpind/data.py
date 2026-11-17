import lib16inpind

FULL_NAME = "Sixteen INPUTS"
LINK = "https://sequentmicrosystems.com/collections/all-io-cards/products/16-universal-inputs-card-for-raspberry-pi"
API = lib16inpind
DOMAIN = "sm16inpind"
NAME_PREFIX = "sm16ii"
SM_MAP = {
    "binary_sensor": {
        "opto": {
            "chan_no": 16,
            "com": {
                "get": "readCh",
            },
        }
    },
}
