# llm-guardrails
Guardrails for LLM Workflows

```sh
    # install packages
    pip install -r requirements.txt
    # configure guardrail hub
    /usr/local/Caskroom/miniconda/base/envs/llm-guardrails/bin/guardrails configure
    /usr/local/Caskroom/miniconda/base/envs/llm-guardrails/bin/guardrails hub install hub://guardrails/valid_range
    /usr/local/Caskroom/miniconda/base/envs/llm-guardrails/bin/guardrails hub install hub://guardrails/uppercase
    /usr/local/Caskroom/miniconda/base/envs/llm-guardrails/bin/guardrails hub install hub://guardrails/lowercase
    /usr/local/Caskroom/miniconda/base/envs/llm-guardrails/bin/guardrails hub install hub://guardrails/one_line
    /usr/local/Caskroom/miniconda/base/envs/llm-guardrails/bin/guardrails hub install hub://guardrails/detect_pii
```