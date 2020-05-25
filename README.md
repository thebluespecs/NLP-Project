Load this Jupyter Notebook into Google Colaboratory and run all the cells for the text generation for alternate endings of GOT.

Left to do: Finetune a few parameters for which clone: https://github.com/nshepperd/gpt-2 and finetune train.py arguments for better results or finetune the notebook call of the train function. I suggest cloning, cleaning and editing the code for what we need. 

Also, look into the use case of top_p and top_k sampling techniques as they will be responsible for sampling the next word which means the surprise factor of the generated text depends on it. A bit of a reference can be taken from: https://colab.research.google.com/github/huggingface/blog/blob/master/notebooks/02_how_to_generate.ipynb
