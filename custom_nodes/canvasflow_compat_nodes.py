class FloatConstant:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("FLOAT", {"default": 1.0, "min": -1000000.0, "max": 1000000.0, "step": 0.01})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "run"
    CATEGORY = "canvasflow/compat"

    def run(self, value):
        return (float(value),)


NODE_CLASS_MAPPINGS = {
    "FloatConstant": FloatConstant,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FloatConstant": "Float Constant",
}
