# tfhub-bert
Loading Bert using Tensorflow Hub

1. Setup local cache directory for tensorflow hub
```bash
mkdir "${HOME}/tf-hub-cache"

cp ~/.bash_profile ~/.bash_profile.bkup
echo 'export TFHUB_CACHE_DIR="${HOME}/tf-hub-cache"' >> ~/.bash_profile
source "${HOME}/.bash_profile"

echo $TFHUB_CACHE_DIR
```

2. Create a new environment and install requirements
```bash
conda create -n bert python=3.7
source activate bert

(bert) pip install -r requirements.txt
```

3. Download Bert Model, and copy vocab file. Replace URL and model by checking `descriptor.txt`
```bash
python download_bert.py
cp $TFHUB_CACHE_DIR/ecd2596ce849110246602e3d4d81e2d9719cb027/assets/vocab.txt .
```
