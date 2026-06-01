import gymnasium as gym
from stable_baselines3 import PPO
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
    name_prefix="ppo_lunarlander",
)

# 4. Initialize Model
model = PPO(
    "MlpPolicy",
    env,
    verbose=0,
    tensorboard_log=log_dir,
    
    learning_rate=0.001,
    batch_size=128,
    gamma=0.99,
    policy_kwargs=dict(net_arch=[256, 256])
)

# 5. Train the Model

# Run TensorBoard in a new terminal to visualize training progress
# tensorboard --logdir ./DRL_logs/tboard/
# open the URL that it give you in your browser

model.learn(
    total_timesteps=300_000,
    callback=checkpoint_callback,
    progress_bar=True#,
    #tb_log_name="DQN_run_1" # Custom name for this run in TensorBoard
)



# 6. Save final model
model.save("ppo_final_model")

env.close()