# import openvino_genai as ov_genai

# model_path = './models/deepseek-ai-DeepSeek-R1-0528-Qwen3-8B'
# device = 'CPU'

# pipe = ov_genai.LLMPipeline(models_path=model_path, device=device)
# print(pipe.generate('What is OpenVINO?', max_length=200))

from optimum.intel import OVModelForCausalLM

model_path = './models/deepseek-ai-DeepSeek-R1-0528-Qwen3-8B'

model = OVModelForCausalLM.from_pretrained(model_path)
model.forward