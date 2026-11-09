# Derivation of the gradient of the log softmax policy with linear action preferences

See Sutton & Barto, Chapter 13.

The policy gradient theorem allows us to estimate the gradient from sampled actions:

$$\nabla J(\theta) \propto \sum_s \mu(s) \sum_a q_\pi(s,a) \nabla\pi(a|s,\theta)
$$

REINFORCE shows that:
$$\nabla J(\theta) \propto E_\pi[G_t \nabla \ln \pi(a|s,\theta)] 
$$

For a softmax policy with linear action preferences this gradient is is:

$$\nabla \ln \pi(a|s,\theta) = x(s,a) - \sum_b \pi(b|s,\theta)\,x(s,b)$$

This document shows the derivation of the gradient.

## Setup

Each state-action pair has a feature vector x(s,a), and the **action preference** is linear in θ:

$$h(s,a,\theta) = \theta^\top x(s,a)$$

The policy is the softmax over preferences:

$$\pi(a|s,\theta) = \frac{e^{\theta^\top x(s,a)}}{\sum_b e^{\theta^\top x(s,b)}}$$

## Step 1: Take the log

$$\ln \pi(a|s,\theta) = \theta^\top x(s,a) - \ln \sum_b e^{\theta^\top x(s,b)}$$

The log turns the ratio into a difference, which is why we differentiate ln π rather than π itself.

## Step 2: Differentiate each term with respect to θ

**First term.** The gradient of a linear function is its coefficient vector:

$$\nabla_\theta\, \theta^\top x(s,a) = x(s,a)$$

**Second term.** Use the chain rule on ln(·), then on the exponentials:

$$\nabla_\theta \ln \sum_b e^{\theta^\top x(s,b)} = \frac{1}{\sum_{b'} e^{\theta^\top x(s,b')}} \sum_b e^{\theta^\top x(s,b)}\, x(s,b)$$

## Step 3: Recognize the softmax probabilities

Move the normalizing constant inside the sum:

$$\sum_b \frac{e^{\theta^\top x(s,b)}}{\sum_{b'} e^{\theta^\top x(s,b')}}\, x(s,b) = \sum_b \pi(b|s,\theta)\,x(s,b)$$

## Step 4: Combine

$$\boxed{\nabla_\theta \ln \pi(a|s,\theta) = x(s,a) - \sum_b \pi(b|s,\theta)\,x(s,b)}$$

## Interpretation

- $x(s,a)$ is the feature vector of the action actually taken.
- $\sum_b \pi(b|s,\theta) x(s,b)$ is the **expected feature vector** under the current policy, $E_\pi[x(s,\cdot)$].
- The gradient is therefore "what you did minus what you'd do on average."

Plugged into REINFORCE, $\theta \leftarrow \theta + \alpha G_t \nabla ln \pi(A_t|S_t,\theta)$, a positive return pushes $\theta$ toward features of the chosen action, and a negative return pushes away. 


Modified from Source: Claude.ai