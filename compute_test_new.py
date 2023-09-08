import time


def choice_01(data):
    v_value_list = [1, 2, 3, 4, 5]
    choice_flag = data.get('flag', 0)
    v = data.get('c1v1', v_value_list[0])
    start_value = None

    if choice_flag:
        if choice_flag == -1:
            v_index = v_value_list.index(v)
            if 0 <= v_index < len(v_value_list) - 1:
                v = v_value_list[v_index + 1]
            else:
                v = v_value_list[-1]
                choice_flag = 1
        elif choice_flag == 1:
            v_index = v_value_list.index(v)
            if 0 < v_index <= len(v_value_list):
                v = v_value_list[v_index - 1]
            else:
                v = v_value_list[0]
                choice_flag = -1
        else:
            assert ValueError('未知flag取值！！')
    else:
        v = v_value_list[0]
        choice_flag = -1
        start_value = v

    if start_value is not None:
        choice_res = {
            'flag': choice_flag,
            'start_value': start_value,
            'c1v1': v
        }
    else:
        choice_res = {
            'flag': choice_flag,
            'c1v1': v
        }
    return choice_res


def choice_02(data):
    v_value_list = [1, 2, 3, 4, 5]
    choice_flag = data.get('flag', 0)
    v = data.get('c1v2', v_value_list[0])
    start_value = None
    
    if choice_flag:
        if choice_flag == -1:
            v_index = v_value_list.index(v)
            if 0 <= v_index < len(v_value_list) - 1:
                v = v_value_list[v_index + 1]
            else:
                v = v_value_list[-1]
                choice_flag = 1
        elif choice_flag == 1:
            v_index = v_value_list.index(v)
            if 0 < v_index <= len(v_value_list):
                v = v_value_list[v_index - 1]
            else:
                v = v_value_list[0]
                choice_flag = -1
        else:
            assert ValueError('未知flag取值！！')
    else:
        v = v_value_list[0]
        choice_flag = -1
        start_value = v

    if start_value is not None:
        choice_res = {
            'flag': choice_flag,
            'start_value': start_value,
            'c1v2': v
        }
    else:
        choice_res = {
            'flag': choice_flag,
            'c1v2': v
        }
    return choice_res


def choice_03(data):
    v_value_list = [1, 2, 3, 4, 5]
    choice_flag = data.get('flag', 0)
    v = data.get('c2v1', v_value_list[0])
    start_value = None

    if choice_flag:
        if choice_flag == -1:
            v_index = v_value_list.index(v)
            if 0 <= v_index < len(v_value_list) - 1:
                v = v_value_list[v_index + 1]
            else:
                v = v_value_list[-1]
                choice_flag = 1
        elif choice_flag == 1:
            v_index = v_value_list.index(v)
            if 0 < v_index <= len(v_value_list):
                v = v_value_list[v_index - 1]
            else:
                v = v_value_list[0]
                choice_flag = -1
        else:
            assert ValueError('未知flag取值！！')
    else:
        v = v_value_list[0]
        choice_flag = -1
        start_value = v

    if start_value is not None:
        choice_res = {
            'flag': choice_flag,
            'start_value': start_value,
            'c2v1': v
        }
    else:
        choice_res = {
            'flag': choice_flag,
            'c2v1': v
        }
    return choice_res


def choice_04(data):
    v_value_list = [1, 2, 3, 4, 5]
    choice_flag = data.get('flag', 0)
    v = data.get('c2v2', v_value_list[0])
    start_value = None

    if choice_flag:
        if choice_flag == -1:
            v_index = v_value_list.index(v)
            if 0 <= v_index < len(v_value_list) - 1:
                v = v_value_list[v_index + 1]
            else:
                v = v_value_list[-1]
                choice_flag = 1
        elif choice_flag == 1:
            v_index = v_value_list.index(v)
            if 0 < v_index <= len(v_value_list):
                v = v_value_list[v_index - 1]
            else:
                v = v_value_list[0]
                choice_flag = -1
        else:
            assert ValueError('未知flag取值！！')
    else:
        v = v_value_list[0]
        choice_flag = -1
        start_value = v

    if start_value is not None:
        choice_res = {
            'flag': choice_flag,
            'start_value': start_value,
            'c2v2': v
        }
    else:
        choice_res = {
            'flag': choice_flag,
            'c2v2': v
        }
    return choice_res


def opt_01(data):
    opt_flag = 1
    a = data['c1v1']
    b = data['c1v2']
    
    opt_res = {'c1v3': a * b, 'flag': opt_flag}
    return opt_res


def opt_02(data):
    opt_flag = 1
    a = data['c1v2']
    b = data['c1v3']

    opt_res = {'c1v4': a * b, 'flag': opt_flag}
    return opt_res


def opt_03(data):
    opt_flag = 1
    a = data['c2v1']
    b = data['c2v2']

    opt_res = {'c2v3': a * b, 'flag': opt_flag}
    return opt_res


def opt_04(data):
    opt_flag = 1
    a = data['c2v1']
    b = data['c2v3']

    opt_res = {'c2v4': a * b, 'flag': opt_flag}
    return opt_res


def judge_01(data):
    judge_flag = 0
    a = data['c1v3']
    b = data['c1v4']
    v = a * b

    if 125 < v < 1000:
        judge_flag = 1

    judge_res = {'cv1': v, 'flag': judge_flag}
    return judge_res


def judge_02(data):
    judge_flag = 0
    a = data['c2v3']
    b = data['c2v4']
    v = a * b

    if 150 < v < 650:
        judge_flag = 1

    judge_res = {'cv2': v, 'flag': judge_flag}
    return judge_res


def judge_total(data):
    judge_flag = 0
    a = data['cv1']
    b = data['cv2']
    v = a * b
    
    if 4900 < v < 35000:
        judge_flag = 1

    judge_res = {'cv': v, 'flag': judge_flag}
    return judge_res


def reset_choice_func_dict(choice_func_dict):
    _ = choice_func_dict
    _['before_reset_main_first_value_count'] = _['main_first_value_count']
    _['before_reset_main_first_value'] = _['main_first_value']
    _['before_reset_flag'] = _['flag']
    
    _['main_first_value_count'] = 0
    _['main_first_value'] = None
    _['flag'] = 0
    

def begin(m_id, running_list, func_list):
    print('Doing Something. Mission ID: %s' % m_id)
    next_begin_func_index = 0
    end_flag = 0
    res_dict = dict()
    mission_flag = 0
    start_flag = 1
    restart_flag = 0
    run_msg = '未知状态'
    running_list_len = len(running_list)
    
    while not end_flag:
        # if start_flag:
        #     print('Start!')
        #
        # if restart_flag:
        #     print('Restart!')

        for i in range(next_begin_func_index, running_list_len):
            func_dict = running_list[i]
            func = func_dict['func']
            func_name = func.__name__
            if func_name.startswith('opt_'):
                raw_data = {x: res_dict[x] for x in func_dict['raw_data_keys']}
                func_res = func(raw_data)
                opt_flag = func_res.pop('flag')
                if opt_flag:
                    res_dict.update(func_res)
            elif func_name.startswith('choice_'):
                flag_data = {'flag': func_dict.get('flag', 0)}
                raw_data = {
                    x: res_dict[x]
                    for x in func_dict['raw_data_keys']
                    if x in res_dict
                }

                raw_data.update(flag_data)

                func_res = func(raw_data)

                choice_flag = func_res.pop('flag')

                choice_res_dict = {
                    k: func_res[k]
                    for k in func_dict['res_data_keys']
                    if k != 'flag' and k != 'star_value'
                }

                res_dict.update(choice_res_dict)

                print('res_dict', res_dict)

                func_dict['flag'] = choice_flag

                if not func_dict.get('main_first_value_count', 0):
                    if 'start_value' in func_res:
                        func_dict['main_first_value'] = func_res.pop('start_value')
                    func_dict['main_first_value_count'] += 1
                elif res_dict[func_dict['main_key']] == func_dict['main_first_value']:
                    func_dict['main_first_value_count'] += 1
                else:
                    pass

            elif func_name.startswith('judge_'):
                # 给每个判断函数添加当前的第一个选择函数，当当前第一个选择函数选完值并且判断函数还未满足时，如果是子判断函数，应该让主判断函数
                # 中的"now_main_choice_func_index"去前一个值，而如果在主判断函数中，就应该结束整个过程，并且整个过程失败，给出错误信息。
                judge_continue = 0
                if 'judge_func_index_list' in func_dict and 'choice_func_index_list' not in func_dict:
                    choice_func_index_list = []
                    for ji in func_dict['judge_func_index_list']:
                        choice_func_index_list.extend(running_list[ji]['choice_func_index_list'])
                    func_dict['choice_func_index_list'] = choice_func_index_list

                raw_data = {x: res_dict[x] for x in func_dict['raw_data_keys']}
                func_res = func(raw_data)

                judge_keys = list(func_res.keys()).sort()
                judge_set_res_keys = func_dict['res_data_keys'].sort()
                if judge_keys != judge_set_res_keys:
                    raise KeyError(f'判断结果和判断函数的key不一致，judge_res_keys：{judge_keys}，'
                                   f'judge_set_res_keys：{judge_set_res_keys}')

                judge_flag = func_res.pop('flag')
                res_dict.update(func_res)

                if judge_flag:      # 表示判断通过
                    func_dict['self_judge'] = 0
                    run_msg = '判断通过。判断函数名称：%s，判断函数在总的函数列表中的执行顺序：%s。' % (func_name, func_list.index(func_name))
                    mission_flag = 1
                    show_info(run_msg)
                    if i == running_list_len - 1:
                        mission_flag = 1
                        end_flag = 1
                        break
                    else:
                        continue

                __end_flag = 0  # _ef
                judge_func_choice_func_index_list = func_dict['choice_func_index_list']

                for __func_index in judge_func_choice_func_index_list[::-1]:
                    __func_dict = running_list[__func_index]
                    if __func_dict['main_first_value_count'] != 2:
                        next_begin_func_index = __func_index

                        if not __func_dict['flag'] and __func_dict['main_first_value'] is not None:
                            __func_dict['flag'] = -1

                        __end_flag = 1
                        break
                    else:
                        if __func_index == judge_func_choice_func_index_list[0]:
                            print('判断是继续还是就此退出！！！')
                            reset_choice_func_dict(__func_dict)

                            if func_dict.get('self_judge', 1):
                                run_msg = f'未找到合适的值，判断函数：{func_name}\n{"*" * 30}'
                                end_flag = 1
                                __end_flag = 1
                            else:
                                string = '还得继续来，等我恢复几个函数先！'
                                show_info(string)
                                for ii in judge_func_choice_func_index_list:
                                    __fc = running_list[ii]
                                    __fc['main_first_value_count'] = __fc['before_reset_main_first_value_count']
                                    __fc['main_first_value'] = __fc['before_reset_main_first_value']
                                    __fc['flag'] = 0

                                judge_continue = 1
                                string = '恢复完成，继续！'
                                show_info(string)
                            break
                        else:
                            print('重置前函数', __func_dict)
                            reset_choice_func_dict(__func_dict)
                            print('重置后函数', __func_dict)

                if __end_flag:
                    break

                if judge_continue:
                    continue

            elif func_name == 'show_info':
                func(func_dict['info'])
            else:
                pass

            if i == running_list_len - 1:
                mission_flag = 1
                end_flag = 1
                break

            # time.sleep(0.1)

        if end_flag:
            print(f'最终结果：{res_dict}')

        start_flag = 0
        restart_flag = 1

    return mission_flag, run_msg, res_dict


def show_info(info_string):
    print(info_string)


if __name__ == '__main__':
    running_info_list = [
        {'func': show_info, 'info': '第一步'},   # 此函数中可以写提示/打印相关的信息
        {'func': choice_01, 'raw_data_keys': ['flag', 'c1v1'], 'main_key': 'c1v1', 'res_data_keys':['c1v1'],
         'main_first_value_count': 0, 'main_first_value': None, 'flag': 0},
        {'func': choice_02, 'raw_data_keys': ['flag', 'c1v2'], 'main_key': 'c1v2', 'res_data_keys':['c1v2'],
         'main_first_value_count': 0, 'main_first_value': None, 'flag': 0},
        {'func': opt_01, 'raw_data_keys': ['c1v1', 'c1v2'], 'res_data_keys': ['c1v3']},
        {'func': opt_02, 'raw_data_keys': ['c1v2', 'c1v3'], 'res_data_keys': ['c1v4']},
        {'func': judge_01, 'raw_data_keys': ['c1v3', 'c1v4'], 'res_data_keys': ['flag', 'cv1'],
         'choice_func_index_list': [1, 2]},
        {'func': show_info, 'info': '第二步'},
        {'func': choice_03, 'raw_data_keys': ['flag', 'c2v1'], 'main_key': 'c2v1', 'res_data_keys': ['c2v1'],
         'main_first_value_count': 0, 'main_first_value': None, 'flag': 0},
        {'func': choice_04, 'raw_data_keys': ['flag', 'c2v2'], 'main_key': 'c2v2', 'res_data_keys': ['c2v2'],
         'main_first_value_count': 0, 'main_first_value': None, 'flag': 0},
        {'func': opt_03, 'raw_data_keys': ['c2v1', 'c2v2'], 'res_data_keys': ['c2v3']},
        {'func': opt_04, 'raw_data_keys': ['c2v1', 'c2v3'], 'res_data_keys': ['c2v4']},
        {'func': judge_02, 'raw_data_keys': ['c2v3', 'c2v4'], 'res_data_keys': ['flag', 'cv2'],
         'choice_func_index_list': [7, 8]},
        {'func': judge_total, 'raw_data_keys': ['cv1', 'cv2'], 'res_data_keys': ['flag', 'cv'],
         'choice_func_index_list': [1, 2, 7, 8], 'judge_func_index_list': [5, 11]},
    ]

    running_func_name_list = [x['func'].__name__ for x in running_info_list]
    
    mission_id = 'FACE_1231343545123'
    t1 = time.time()
    flag, msg, res = begin(mission_id, running_info_list, running_func_name_list)
    t2 = time.time()
    print('-' * 30)
    print('任务%s执行情况：' % mission_id)
    print('任务执行标志：', flag)

    print('任务执行消息：', msg)
    print('任务执行结果：', res)
    print('任务执行耗时：%.2fs' % (t2 - t1))