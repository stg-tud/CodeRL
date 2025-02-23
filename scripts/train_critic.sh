#
# Copyright (c) 2022, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#

# Reads:
# ${train-path}/????/{question.txt, solutions.json, gen_solutions.json}
# Optionally reads:
# ${train-path}/????/starter_code.py
# Writes:
# ${save_dir}/args.json
# ${save_dir}/final_checkpoint/*
# ${save_dir}/*/*

# Run code in debugging mode (without deepspeed)
python \
  train.py \
  --batch-size-per-replica 8 --grad-acc-steps 1 \
  --epochs 10 --lr 2e-5 \
  --save-freq 1000 --log-freq 10 --save_total_limit 5 \
  --fp16 \
  --tuning_mode critic --model codet5-base \
  --db
