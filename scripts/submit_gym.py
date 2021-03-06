from __future__ import print_function
from __future__ import absolute_import
import argparse
import os
import os.path as osp
import gym
from rllab.viskit.core import load_params

if __name__ == "__main__":
    # rl_gym.api_key = 'g8JOpnNVmcjMShBiFtyji2VWX3P2uCzc'
    if 'OPENAI_GYM_API_KEY' not in os.environ:
        raise ValueError("OpenAi Gym API key not configured. Please register an account on https://gym.openai.com and"
                         " set the OPENAI_GYM_API_KEY environment variable, and try the script again.")

    parser = argparse.ArgumentParser()
    parser.add_argument('log_dir', type=str,
                        help='path to the logging directory')
    args = parser.parse_args()
    snapshot_dir = osp.abspath(osp.join(args.log_dir, ".."))
    params_file_path = osp.join(snapshot_dir, "params.json")
    params_json = load_params(params_file_path)
    algo_name = params_json['json_args']['algo']['_name'].split(".")[-1]
    gym.upload(args.log_dir, algorithm_id=algo_name)
