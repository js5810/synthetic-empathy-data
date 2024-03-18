#!/bin/bash
torchrun --nproc_per_node 1 chat_completion.py     --ckpt_dir llama-2-7b-chat/     --tokenizer_path tokenizer.model     --max_seq_len 4096 --max_batch_size 1
