def clean_csv(data_file):
    df = None
    #   receives a csv and changes it to a format that may be used for naive_bayes
    #	creates and returns a data frame of the cleaned data.
    #	calculates and records total_score in a column named
    #	then returns the cleaned data frame.
    return df


def get_passing_score_by_percentile(list_of_scores, percentile):
    minimum_score = 0
    #   returns the minimum score on the test to be at or above the specified percentile
    # 	with reference to the list of scores.
    return minimum_score


def add_passed_to_data_frame_and_assign_correct_values(data_frame, passing_score):
    df = None
    # returns data frame with passed
    return df


def create_model():
    m = None
    # returns the model you intend to use for the remainder of your code
    return m


def get_fit_model(Xs, y):
    fit = None
    # returns the fit for a model
    return fit


def select_variables_for_fit(data_frame):
    Xs = None
    y = None
    #   returns list of indexes or names which will be used to fit your model,
    #	and returns name of outcome variable (in this case 'passed')
    return Xs, y


def assess_fit(fit, Xs, y):
    accuracy = None
    # returns the accuracy of the model fit as a proportion.
    return accuracy

def interface(file_name, percentile=50):
    ret = []
    df = ret.append(clean_csv(file_name))
    ret.append(get_passing_score_by_percentile(df["score"], percentile))
    ret.append(add_passed_to_data_frame_and_assign_correct_values(df))
    m = create_model()
    ret.append(m)
    selected = select_variables_for_fit(df)
    Xs = df[selected[0]]
    y = df[selected[1]]
    ret.append(Xs, y)
    fit = get_fit_model(df[Xs, y])
    ret.append(fit)
    return ret


def run_test(train_set, test_set=False):
    Xs_Y = 5
    FIT = 6
    t1 = interface(train_set)
    if test_set:
        t2 = interface(test_set)
        fit = t1[FIT]
        t2_df = t2[0]
        selectedXs = t1[Xs_Y][0]
        selectedY = t1[Xs_Y][1]
        r = assess_fit(fit, t2_df[selectedXs], t2_df[selectedY])
        print(round(r * 100), 2)