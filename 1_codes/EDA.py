import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import icons, styles

import pandas as pd

def eda(pth: str) -> tuple:
  train_df = pd.read_csv(os.path.join(pth, "train.csv"))
  train_df.name = "Train"
  test_df = pd.read_csv(os.path.join(pth, "test.csv"))
  test_df.name = "Test"
  if train_df.columns.tolist() == test_df.columns.tolist():
    cols = train_df.columns.tolist()

    # ====== columns ======
    print(f"{icons.TICK} There are {styles.BOLD}{len(cols)} identical columns{styles.END} acros both datasets:")
    for col in cols:
      print(f"\t{icons.BULLET} {col}")

    # ====== missingness ======
    if test_df.isna().sum().any() or train_df.isna().sum().any():
      print("mising columns exist")
    else:
      print(f"{icons.TICK} {styles.BOLD}No mising values{styles.END} in either datasets.")

    # ====== sample counts ======
    if len(train_df) == len(test_df):
      print(f"{icons.TICK} {styles.BOLD}Both{styles.END} of the datasets have {styles.BOLD}{len(train_df)}{styles.END} samples.")
    else:
      print(f"{icons.TICK} {styles.BOLD}Train:{styles.END} {len(train_df)} samples {icons.BULLET} {styles.BOLD}Test:{styles.END} {len(test_df)} samples")
    
    # ====== data types ======
    # TODO: do not print dtypes, instead check it and print something like, "all of them str".
    train_dtypes = train_df.dtypes.astype(str).tolist()
    test_dtypes = test_df.dtypes.astype(str).tolist()
    if train_dtypes == test_dtypes:
      if len(set(train_dtypes)) == 1:
        print(f"{icons.TICK} All columns are {styles.BOLD}{train_dtypes[0]}{styles.END} type in both datasets.")
      else:
        print(f"{icons.TICK} Column types are {styles.BOLD}identical{styles.END} across both datasets:")
        for col, dtype in zip(cols, train_dtypes):
          print(f"\t{icons.BULLET} {styles.BOLD}{col}{styles.END}: {dtype}")
    else:
      print(f"{icons.WARNING} {styles.RED}{styles.BOLD}Column types do not match between datasets:{styles.END}")
      for col in cols:
        tr = str(train_df[col].dtype)
        te = str(test_df[col].dtype)
        if tr != te:
          print(f"\t{icons.BULLET} {styles.BOLD}{col}{styles.END}: Train={tr}, Test={te}")
    # ====== uniqueness ====== 
    print(f"{styles.BOLD} {styles.UNDERLINE}Column Summaries:{styles.END}")
    for df in (train_df, test_df):
      print(f"{styles.BOLD}{df.name} Dataset:{styles.END}")
      t = df.describe().T
      for i in t.index:
        print(f"    {icons.BULLET} {styles.BOLD}{i}{styles.END}: {t.loc[i, 'unique']} distinct values, {t.loc[i, 'count']} non-null rows")
      del t

  else:
    print("Columns of train dataset:")
    print(train_df.columns.tolist())
    print("Columns of test dataset:")
    print(test_df.columns.tolist())
  return train_df, test_df


if __name__ == "__main__":
  eda()
