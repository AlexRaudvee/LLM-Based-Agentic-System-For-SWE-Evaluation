from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLM:
    def __init__(self, model_name: str = "Qwen/Qwen3-0.6B"):
        self.tok = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, torch_dtype="auto", device_map="auto"
        )
        self.messages = []

    def generate(self, prompt: str, max_new_tokens: int = 1000) -> str:
    
        self.messages = [
            {"role": "user", "content": prompt}
        ]
        
        text = self.tok.apply_chat_template(
            self.messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False # Switches between thinking and non-thinking modes. Default is True.
        )
        
        model_inputs = self.tok([text], return_tensors="pt").to(self.model.device)

        # conduct text completion
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=32768
        )
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

        content = self.tok.decode(output_ids[index:], skip_special_tokens=True).strip("\n")


        # return only the completion after the prompt
        return text[len(self.tok.decode(inputs["input_ids"][0], skip_special_tokens=True)):]
