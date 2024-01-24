# Borderlands2PS3ProfileEditor
Python tool to modify Borderlands 2 Profile for PS3

## Instructions
1. Download Python Files and example config
   1. `payload_lib`, `config.ini` and `update_payload.py`
2. Get save from PS3    
2. Use 'Bruteforce Save Data' to decrypt your PS3 Profile file.
    1. *Before decrypting* - click the verify PFD button. If this fails, it means that one of your config settings is not correct. e.g. for me, I had the wrong console id; I was using the PSID but should have used the IDPS
3. Edit `config.ini`
    1. BarStat values are percentages; the tool currently doesn't prevent invalid values, so don't put in massive values
    2. Golden Keys is limited to 752. (but you can always redo the edit if you run out)    
    4. If you don't want to update a field just comment it out
    5. For now I've limited features to BarStats, BarRank, BarTokens and GoldenKeys as this is what most people are interested in; FOV was a bouns as I was curious if it would work
4. Run the tool

       python3 update_payload.py --config config.ini --payload <path to decrpyted PAYLOAD>
   
   This will create a new `PAYLOAD.new` file in the same location as `PAYLOAD`.
6. Replace `PAYLOAD` with `PAYLOAD.new`
7. Encrypt save using Brutefroce Save Data
8. Copy Save back to PS3

## Screenshots
I used RPCS3 for this imagines
