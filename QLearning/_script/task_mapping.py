task_dict = {'airfoil': 'reg', 'amazon_employee': 'cls', 'ap_omentum_ovary':
    'cls', 'bike_share': 'reg', 'german_credit': 'cls', 'higgs': 'cls',
             'housing_boston': 'reg', 'ionosphere': 'cls', 'lymphography': 'cls',
             'messidor_features': 'cls', 'openml_620': 'reg', 'pima_indian': 'cls',
             'spam_base': 'cls', 'spectf': 'cls', 'svmguide3': 'cls',
             'uci_credit_card': 'cls', 'wine_red': 'cls', 'wine_white': 'cls',
             'openml_586': 'reg', 'openml_589': 'reg', 'openml_607': 'reg',
             'openml_616': 'reg', 'openml_618': 'reg', 'openml_637': 'reg', 'smtp':
                 'det', 'thyroid': 'det', 'yeast': 'det', 'wbc': 'det', 'mammography': 'det'
             }
task_type = {'reg', 'cls', 'det', 'rank'}
task_measure = {'reg': 'rae', 'cls': 'f1', 'det': 'ROC AUC Score', 'rank':
    'auprc'}
state_rep = {'mds', 'gcn', 'ae', 'mds+ae', 'mds+ae+gcn'}
support_rl_method = {'dqn', 'ddqn', 'dueling_dqn', 'dueling_ddqn'}
base_path = './data/processed/'

if __name__ == '__main__':
    import os

    print(os.curdir)
    base = './data/processed/'
    for name, task in task_dict.items():
        if not os.path.exists(base + name + '.hdf'):
            print(name)
