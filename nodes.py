import json

class ParsePrompt:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {
            "vlm_output": ("STRING", {
                "default": "",
                "multiline": False,
                "lazy": False
                }),
            "nametag": ("STRING", {
                "default": "",
                "multiline": False,
                "lazy": False
            })
        }}
    
    
    RETURN_TYPES = ("STRING",)

    FUNCTION ="run"

    CATEGORY = "CodyCustom"

    def run(self, vlm_output, nametag):
        json_string = vlm_output[vlm_output.index('{'):vlm_output.index('}') + 1]
        info = json.loads(json_string)
        print(info)
        prompt = f"Photorealistic full-length portrait of {info["race_or_ethnicity"]} man with no eyebrows, {info["hair_length"]} {info["hair_color"]} hair, small eyes, as solarpunk fortnite character, looking straight forward at camera. Large nametag on uniform says '{nametag}'. Photorealistic face. Solarpunk village in background. No eyebrows. Missing eyebrows, thin eyebrows. Small eyebrows."
        return (prompt,)
    


class StringCombine:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "string1": ("STRING", {
                    "default": "",
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "lazy": False
                }),
                "string2": ("STRING", {
                    "default": "",
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "lazy": False
                }),
                "separator": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "lazy": False
                })
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION ="run"

    CATEGORY = "CodyCustom"

    def run(self, string1, string2, separator):
        new_string = f"{string1}{separator}{string2}"
        return (new_string,)
