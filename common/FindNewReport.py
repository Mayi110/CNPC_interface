import os

def new_report():
    '''
    找到最细的报告并返回
    :return:
    '''
    base_dir = os.path.dirname(os.path.dirname(__file__))
    report_dir = os.path.join(base_dir,'resultreport')
    lists = os.listdir(report_dir)

    lists.sort(key=lambda fn: os.path.getmtime(report_dir+'\\'+fn))
    new_file = os.path.join(report_dir,lists[-1])
    return new_file
