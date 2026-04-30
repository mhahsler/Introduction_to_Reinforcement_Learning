import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import CheckpointCallback
import os

# 1. Create Environment
env = gym.make("LunarLander-v3")

# 2. Set up TensorBoard log directory and Checkpoint saving
log_dir = "./DRL_logs/tboard/"
model_dir = "./DRL_logs/models/"
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# 3. Define Callback for saving checkpoints
checkpoint_callback = CheckpointCallback(
    save_freq=5000, # Save every 5000 steps
    save_path=model_dir,
    name_prefix="dqn_lunarlander",
)

# 4. Initialize Model
model = DQN(
    "MlpPolicy",
    env,
    verbose=0,
    tensorboard_log=log_dir,
    
    learning_rate=0.001,
    buffer_size=50_000,
    batch_size=128,
    gamma=0.99,
    target_update_interval=250,
    exploration_fraction=0,
    exploration_final_eps=0.3,  # keep a fixed exploration rate for now
    policy_kwargs=dict(net_arch=[256, 256])
)

# 5. Train the Model
model.learn(
    total_timesteps=300_000,
    callback=checkpoint_callback,
    progress_bar=True#,
    #tb_log_name="DQN_run_1" # Custom name for this run in TensorBoard
)

# Run TensorBoard in a new terminal to visualize training progress
# tensorboard --logdir ./DRL_logs/tboard/
# open the URL that it give you in your browser

# 6. Save final model
model.save("dqn_final_model")

env.close()