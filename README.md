# tfhub-bert
1. Setup local cache directory for tensorflow hub
    ```bash
    mkdir "${HOME}/tf-hub-cache"

    cp ~/.bash_profile ~/.bash_profile.bkup
    echo 'export TFHUB_CACHE_DIR="${HOME}/tf-hub-cache"' >> ~/.bash_profile
    source "${HOME}/.bash_profile"
    
    echo $TFHUB_CACHE_DIR
    ```

2. Create a new [conda](https://www.anaconda.com/distribution/) environment (let's call it `bert`) and install requirements
    ```bash
    conda create -n bert python=3.7
    source activate bert
    
    (bert) pip install -r requirements.txt
    ```
    NOTE: if `source activate bert` does not work, try `conda activate bert`

3. Download a Bert Model, and copy vocab file. Feel free to replace BERT URL form [list of available modules](https://tfhub.dev/s?q=bert). You would also need to change the local vocab path accordingly.
    ```bash
    python download_bert.py
    cp $TFHUB_CACHE_DIR/ecd2596ce849110246602e3d4d81e2d9719cb027/assets/vocab.txt .
    ```

4. Get [tokenization.py](https://github.com/google-research/bert/blob/master/tokenization.py) from the official BERT repository

5. Start jupyter
    ```bash
    jupyter notebook
    ```