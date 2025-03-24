# source_text
#     : description* EOF
#     ;

def gen_source_text(depth=3):
    result = ''
    # description* 表示 description 可以出现零次或多次
    while should_generate_description():
        result += gen_description(depth-1)
    result += 'EOF'
    return result

def should_generate_description():
    # 决定是否继续生成 description，这里以 50% 的概率为例
    return random.choice([True, False])



# description
#     : module_declaration
#     | udp_declaration
#     | config_declaration
#     ;


import random

def gen_description(depth=3):
    # 根据 BNF 规则，description 可以是以下三种之一
    choice = random.choice(['module_declaration', 'udp_declaration', 'config_declaration'])
    if choice == 'module_declaration':
        return gen_module_declaration(depth-1)
    elif choice == 'udp_declaration':
        return gen_udp_declaration(depth-1)
    else:
        return gen_config_declaration(depth-1)



# module_declaration
#     : attribute_instance* module_keyword module_identifier module_parameter_port_list? list_of_port_declarations? ';' module_item* 'endmodule'
#     ;


import random
import string

def gen_module_declaration(depth=3):
    result = ''
    # attribute_instance* : 零次或多次 attribute_instance
    while should_generate_attribute_instance():
        result += gen_attribute_instance(depth-1)
    
    # module_keyword
    result += gen_module_keyword(depth-1) + ' '
    
    # module_identifier
    result += gen_module_identifier(depth-1)
    
    # module_parameter_port_list? : 可选
    if should_generate_module_parameter_port_list():
        result += ' ' + gen_module_parameter_port_list(depth-1)
    
    # list_of_port_declarations? : 可选
    if should_generate_list_of_port_declarations():
        result += ' ' + gen_list_of_port_declarations(depth-1)
    
    # ';'
    result += ';\n'
    
    # module_item* : 零次或多次 module_item
    while should_generate_module_item():
        result += gen_module_item(depth-1)
    
    # 'endmodule'
    result += 'endmodule\n'
    
    return result

# 辅助的控制函数
def should_generate_attribute_instance():
    # 以 30% 的概率生成 attribute_instance
    return random.random() < 0.3

def should_generate_module_parameter_port_list():
    # 以 50% 的概率生成 module_parameter_port_list
    return random.random() < 0.5

def should_generate_list_of_port_declarations():
    # 以 70% 的概率生成 list_of_port_declarations
    return random.random() < 0.7

def should_generate_module_item():
    # 以 60% 的概率继续生成 module_item
    return random.random() < 0.6





# module_keyword
#     : 'module'
#     | 'macromodule'
#     ;


import random

def gen_module_keyword(depth=3):
    return random.choice(['module', 'macromodule'])


# module_parameter_port_list
#     : '#' '(' parameter_declaration (',' parameter_declaration)* ')'
#     ;



import random

def gen_module_parameter_port_list(depth=3):
    result = '#('
    # 生成第一个 parameter_declaration
    result += gen_parameter_declaration(depth-1)
    # 可能有多个 (',' parameter_declaration)
    while should_generate_additional_parameter_declaration():
        result += ', ' + gen_parameter_declaration(depth-1)
    result += ')'
    return result

# 辅助控制函数
def should_generate_additional_parameter_declaration():
    # 以 50% 的概率生成额外的 parameter_declaration
    return random.random() < 0.5





# list_of_port_declarations
#     : '(' port_declaration (',' port_declaration)* ')'
#     | '(' port ( ',' port)+ ')'
#     | '(' port_implicit ')'
#     | '(' port_explicit ')'
#     | '(' ')'
#     ;


import random

def gen_list_of_port_declarations(depth=3):
    # 随机选择一种产生式
    # choice = random.randint(1, 5)
    choice = 1
    if choice == 1:
        # '(' port_declaration (',' port_declaration)* ')'
        result = '('
        result += gen_port_declaration(depth-1)
        while should_generate_additional_port_declaration():
            result += ', ' + gen_port_declaration(depth-1)
        result += ')'
        return result
    elif choice == 2:
        # '(' port ( ',' port)+ ')'
        result = '('
        result += gen_port(depth-1)
        # 至少一个 ',' port
        num_additional_ports = random.randint(1, 3)  # 至少一个
        for _ in range(num_additional_ports):
            result += ', ' + gen_port(depth-1)
        result += ')'
        return result
    elif choice == 3:
        # '(' port_implicit ')'
        return '(' + gen_port_implicit(depth-1) + ')'
    elif choice == 4:
        # '(' port_explicit ')'
        return '(' + gen_port_explicit(depth-1) + ')'
    else:
        # '(' ')'
        return '()'

# 辅助函数
def should_generate_additional_port_declaration(depth=3):
    # 以 50% 的概率生成额外的 port_declaration
    return random.random() < 0.5

# port
#     : port_implicit?
#     | port_explicit
#     ;

import random

def gen_port(depth=3):
    # 根据 BNF 规则，port 可以是以下两种情况之一：
    # 1. 可选的 port_implicit（即可能存在也可能不存在）
    # 2. port_explicit

    # 随机决定使用哪种产生式
    if choose_port_implicit():
        # port_implicit?
        if should_generate_port_implicit():
            return gen_port_implicit(depth-1)
        else:
            # port_implicit 不生成，返回空字符串
            return ''
    else:
        # port_explicit
        return gen_port_explicit(depth-1)

# 辅助函数

def choose_port_implicit(depth=3):
    # 随机决定选择 port_implicit? 或 port_explicit
    # 以 50% 的概率选择 port_implicit?
    return random.random() < 0.5

def should_generate_port_implicit(depth=3):
    # 决定是否生成可选的 port_implicit
    # 以 50% 的概率生成 port_implicit
    return random.random() < 0.5



# port_implicit
#     : port_expression
#     ;


def gen_port_implicit(depth=3):
    return gen_port_expression(depth-1)


# port_explicit
#     : '.' port_identifier '(' port_expression? ')'
#     ;


import random

def gen_port_explicit(depth=3):
    result = '.' + gen_port_identifier(depth-1) + '('
    if should_generate_port_expression():
        result += gen_port_expression(depth-1)
    result += ')'
    return result

# 辅助函数
def should_generate_port_expression(depth=3):
    # 决定是否生成可选的 port_expression
    # 以 50% 的概率生成 port_expression
    return random.random() < 0.5




# port_expression
#     : port_reference
#     | '{' port_reference ( ',' port_reference)* '}'
#     ;

import random

def gen_port_expression(depth=3):
    # 根据 BNF 规则，port_expression 可以是以下两种情况之一：
    # 1. port_reference
    # 2. '{' port_reference ( ',' port_reference)* '}'
    
    # 随机选择一种产生式
    if choose_single_port_reference():
        # 情况 1：port_reference
        return gen_port_reference(depth-1)
    else:
        # 情况 2：'{' port_reference ( ',' port_reference)* '}'
        result = '{'
        result += gen_port_reference(depth-1)
        while should_generate_additional_port_reference():
            result += ', ' + gen_port_reference(depth-1)
        result += '}'
        return result

# 辅助函数
def choose_single_port_reference(depth=3):
    # 随机决定选择单个 port_reference 或组合
    # 以 50% 的概率选择单个 port_reference
    return random.random() < 0.5

def should_generate_additional_port_reference(depth=3):
    # 决定是否生成额外的 port_reference
    # 以 50% 的概率生成
    return random.random() < 0.5


# port_reference
#     : port_identifier ('[' constant_range_expression ']')?
#     ;

import random

def gen_port_reference(depth=3):
    result = gen_port_identifier(depth-1)
    if should_generate_constant_range_expression():
        result += '[' + gen_constant_range_expression(depth-1) + ']'
    return result

# 辅助函数
def should_generate_constant_range_expression(depth=3):
    # 决定是否生成可选的 constant_range_expression
    # 以 50% 的概率生成
    return random.random() < 0.5


# port_declaration
#     : attribute_instance* inout_declaration
#     | attribute_instance* input_declaration
#     | attribute_instance* output_declaration
#     ;


import random

def gen_port_declaration(depth=3):
    result = ''
    # 生成零次或多次 attribute_instance
    while should_generate_attribute_instance():
        result += gen_attribute_instance(depth-1)
    
    # 随机选择一个产生式
    choice = random.choice(['inout_declaration', 'input_declaration', 'output_declaration'])
    if choice == 'inout_declaration':
        result += gen_inout_declaration(depth-1)
    elif choice == 'input_declaration':
        result += gen_input_declaration(depth-1)
    else:
        result += gen_output_declaration(depth-1)
    
    return result

# 辅助函数

def should_generate_attribute_instance(depth=3):
    # 决定是否生成 attribute_instance
    # 以 50% 的概率生成每一个 attribute_instance
    return random.random() < 0.5



# module_item
#     : port_declaration ';'
#     | module_or_generate_item
#     | generate_region
#     | specify_block
#     | attribute_instance* parameter_declaration ';'
#     | attribute_instance* specparam_declaration
#     ;


import random

def gen_module_item(depth=3):
    choice = random.randint(1, 5)
    if choice == 1:
        return gen_port_declaration(depth-1) + ';'
    elif choice == 2:
        return gen_module_or_generate_item(depth-1)
    elif choice == 3:
        return gen_generate_region(depth-1)
    elif choice == 4:
        return gen_specify_block(depth-1)
    elif choice == 5:
        result = ''
        if random.choice([True, False]):
            result += gen_attribute_instance(depth-1) + ' '
        result += gen_parameter_declaration(depth-1) + ';'
        return result
    else:
        result = ''
        if random.choice([True, False]):
            result += gen_attribute_instance(depth-1) + ' '
        result += gen_specparam_declaration(depth-1)
        return result


# module_or_generate_item
#     : attribute_instance* module_or_generate_item_declaration
#     | attribute_instance* local_parameter_declaration ';'
#     | attribute_instance* parameter_override
#     | attribute_instance* continuous_assign
#     | attribute_instance* gate_instantiation
#     | attribute_instance* module_instantiation
#     | attribute_instance* udp_instantiation
#     | attribute_instance* initial_construct
#     | attribute_instance* always_construct
#     | attribute_instance* loop_generate_construct
#     | attribute_instance* conditional_generate_construct
#     ;


import random

def gen_module_or_generate_item(depth=3):
    # 生成 0 到多个 attribute_instance
    num_attrs = random.randint(0, 3)
    attrs = ' '.join([gen_attribute_instance(depth-1) for _ in range(num_attrs)])
    if attrs:
        attrs += ' '  # 添加空格分隔

    choice = random.randint(1, 11)
    if choice == 1:
        return attrs + gen_module_or_generate_item_declaration(depth-1)
    elif choice == 2:
        return attrs + gen_local_parameter_declaration(depth-1) + ';'
    elif choice == 3:
        return attrs + gen_parameter_override(depth-1)
    elif choice == 4:
        return attrs + gen_continuous_assign(depth-1)
    elif choice == 5:
        return attrs + gen_gate_instantiation(depth-1)
    elif choice == 6:
        return attrs + gen_module_instantiation(depth-1)
    elif choice == 7:
        return attrs + gen_udp_instantiation(depth-1)
    elif choice == 8:
        return attrs + gen_initial_construct(depth-1)
    elif choice == 9:
        return attrs + gen_always_construct(depth-1)
    elif choice == 10:
        return attrs + gen_loop_generate_construct(depth-1)
    elif choice == 11:
        return attrs + gen_conditional_generate_construct(depth-1)


# module_or_generate_item_declaration
#     : net_declaration
#     | reg_declaration
#     | integer_declaration
#     | real_declaration
#     | time_declaration
#     | realtime_declaration
#     | event_declaration
#     | genvar_declaration
#     | task_declaration
#     | function_declaration
#     ;


import random

def gen_module_or_generate_item_declaration(depth=3):
    choice = random.randint(1, 10)
    if choice == 1:
        return gen_net_declaration(depth-1)
    elif choice == 2:
        return gen_reg_declaration(depth-1)
    elif choice == 3:
        return gen_integer_declaration(depth-1)
    elif choice == 4:
        return gen_real_declaration(depth-1)
    elif choice == 5:
        return gen_time_declaration(depth-1)
    elif choice == 6:
        return gen_realtime_declaration(depth-1)
    elif choice == 7:
        return gen_event_declaration(depth-1)
    elif choice == 8:
        return gen_genvar_declaration(depth-1)
    elif choice == 9:
        return gen_task_declaration(depth-1)
    elif choice == 10:
        return gen_function_declaration(depth-1)

# parameter_override
#     : 'defparam' list_of_defparam_assignments ';'
#     ;


def gen_parameter_override(depth=3):
    return "defparam " + gen_list_of_defparam_assignments(depth-1) + ";"


# config_declaration
#     : 'config' config_identifier ';' design_statement config_rule_statement* 'endconfig'
#     ;


def gen_config_declaration(depth=3):
    result = "config " + gen_config_identifier(depth-1) + "; " + gen_design_statement(depth-1)
    # 生成 0 到多个 config_rule_statement
    for _ in range(random.randint(0, 3)):
        result += " " + gen_config_rule_statement(depth-1)
    result += " endconfig"
    return result



def gen_design_statement(depth=3):
    result = "design "
    # 生成 0 到多个 design_statement_item
    for _ in range(random.randint(0, 3)):
        result += gen_design_statement_item(depth-1) + " "
    result = result.strip() + ";"
    return result

# design_statement_item
#     : (library_identifier '.')? cell_identifier
#     ;

def gen_design_statement_item(depth=3):
    result = ""
    # 可选生成 (library_identifier '.') 部分
    if random.choice([True, False]):
        result += gen_library_identifier(depth-1) + "."
    result += gen_cell_identifier(depth-1)
    return result

# config_rule_statement
#     : default_clause liblist_clause ';'
#     | inst_clause liblist_clause ';'
#     | inst_clause use_clause ';'
#     | cell_clause liblist_clause ';'
#     | cell_clause use_clause ';'
#     ;

def gen_config_rule_statement(depth=3):
    choice = random.randint(1, 5)
    if choice == 1:
        # default_clause liblist_clause ';'
        return gen_default_clause(depth-1) + " " + gen_liblist_clause(depth-1) + ";"
    elif choice == 2:
        # inst_clause liblist_clause ';'
        return gen_inst_clause(depth-1) + " " + gen_liblist_clause(depth-1) + ";"
    elif choice == 3:
        # inst_clause use_clause ';'
        return gen_inst_clause(depth-1) + " " + gen_use_clause(depth-1) + ";"
    elif choice == 4:
        # cell_clause liblist_clause ';'
        return gen_cell_clause(depth-1) + " " + gen_liblist_clause(depth-1) + ";"
    elif choice == 5:
        # cell_clause use_clause ';'
        return gen_cell_clause(depth-1) + " " + gen_use_clause(depth-1) + ";"


# default_clause
#     : 'default'
#     ;


def gen_default_clause(depth=3):
    return "default"

# inst_clause
#     : 'instance' inst_name
#     ;


def gen_inst_clause(depth=3):
    return "instance " + gen_inst_name(depth-1)

# inst_name
#     : topmodule_identifier ('.' instance_identifier)*
#     ;

def gen_inst_name(depth=3):
    result = gen_topmodule_identifier(depth-1)
    # 随机生成 0 到多个 instance_identifier，前面加点
    for _ in range(random.randint(0, 3)):
        result += "." + gen_instance_identifier(depth-1)
    return result

# cell_clause
#     : 'cell' (library_identifier '.')? cell_identifier
#     ;


def gen_cell_clause(depth=3):
    result = "cell "
    # 可选生成 (library_identifier '.') 部分
    if random.choice([True, False]):
        result += gen_library_identifier(depth-1) + "."
    result += gen_cell_identifier(depth-1)
    return result

# liblist_clause
#     : 'liblist' library_identifier*
#     ;


def gen_liblist_clause(depth=3):
    result = "liblist"
    # 随机生成 0 到多个 library_identifier
    for _ in range(random.randint(0, 3)):
        result += " " + gen_library_identifier(depth-1)
    return result

# use_clause
#     : 'use' (library_identifier '.')? cell_identifier (':' 'config')?
#     ;


def gen_use_clause(depth=3):
    result = "use "
    # 可选生成 (library_identifier '.') 部分
    if random.choice([True, False]):
        result += gen_library_identifier(depth-1) + "."

    result += gen_cell_identifier(depth-1)

    # 可选生成 ': config'
    if random.choice([True, False]):
        result += " : config"

    return result

# local_parameter_declaration
#     : 'localparam' 'signed'? range_? list_of_param_assignments
#     | 'localparam' parameter_type list_of_param_assignments
#     ;


def gen_local_parameter_declaration(depth=3):
    result = "localparam "

    # 50% 概率选择第一种规则，50% 选择第二种规则
    if random.choice([True, False]):
        # 第一种：'localparam' 'signed'? range_? list_of_param_assignments
        if random.choice([True, False]):
            result += "signed "
        if random.choice([True, False]):
            result += gen_range_(depth-1) + " "
    else:
        # 第二种：'localparam' parameter_type list_of_param_assignments
        result += gen_parameter_type(depth-1) + " "

    result += gen_list_of_param_assignments(depth-1)
    return result


# parameter_declaration
#     : 'parameter' 'signed'? range_? list_of_param_assignments
#     | 'parameter' parameter_type list_of_param_assignments
#     ;

def gen_parameter_declaration(depth=3):
    result = "parameter "

    # 50% 概率选择第一种规则，50% 选择第二种规则
    if random.choice([True, False]):
        # 第一种：'parameter' 'signed'? range_? list_of_param_assignments
        if random.choice([True, False]):
            result += "signed "
        if random.choice([True, False]):
            result += gen_range_(depth-1) + " "
    else:
        # 第二种：'parameter' parameter_type list_of_param_assignments
        result += gen_parameter_type(depth-1) + " "

    result += gen_list_of_param_assignments(depth-1)
    return result


# specparam_declaration
#     : 'specparam' range_? list_of_specparam_assignments ';'
#     ;


def gen_specparam_declaration(depth=3):
    result = "specparam "
    
    # 可选生成 range_
    if random.choice([True, False]):
        result += gen_range_(depth-1) + " "
    
    result += gen_list_of_specparam_assignments(depth-1) + ";"
    return result

# parameter_type
#     : 'integer'
#     | 'real'
#     | 'realtime'
#     | 'time'
#     ;

def gen_parameter_type(depth=3):
    return random.choice(["integer", "real", "realtime", "time"])

# inout_declaration
#     : 'inout' net_type? 'signed'? range_? list_of_port_identifiers
#     ;

def gen_inout_declaration(depth=3):
    result = "inout "

    # 可选生成 net_type
    if random.choice([True, False]):
        result += gen_net_type(depth-1) + " "

    # 可选生成 signed
    if random.choice([True, False]):
        result += "signed "

    # 可选生成 range_
    if random.choice([True, False]):
        result += gen_range_(depth-1) + " "

    result += gen_list_of_port_identifiers(depth-1)
    return result

# input_declaration
#     : 'input' net_type? 'signed'? range_? list_of_port_identifiers
#     ;


def gen_input_declaration(depth=3):
    result = "input "

    # 可选生成 net_type
    if random.choice([True, False]):
        result += gen_net_type(depth-1) + " "

    # 可选生成 signed
    if random.choice([True, False]):
        result += "signed "

    # 可选生成 range_
    if random.choice([True, False]):
        result += gen_range_(depth-1) + " "

    result += gen_list_of_port_identifiers(depth-1)
    return result

# output_declaration
#     : 'output' net_type? 'signed'? range_? list_of_port_identifiers
#     | 'output' 'reg' 'signed'? range_? list_of_variable_port_identifiers
#     | 'output' output_variable_type list_of_variable_port_identifiers
#     ;



def gen_output_declaration(depth=3):
    result = "output "

    choice = random.randint(1, 3)
    
    if choice == 1:
        # 'output' net_type? 'signed'? range_? list_of_port_identifiers
        if random.choice([True, False]):
            result += gen_net_type(depth-1) + " "
        if random.choice([True, False]):
            result += "signed "
        if random.choice([True, False]):
            result += gen_range_(depth-1) + " "
        result += gen_list_of_port_identifiers(depth-1)
    
    elif choice == 2:
        # 'output' 'reg' 'signed'? range_? list_of_variable_port_identifiers
        result += "reg "
        if random.choice([True, False]):
            result += "signed "
        if random.choice([True, False]):
            result += gen_range_(depth-1) + " "
        result += gen_list_of_variable_port_identifiers(depth-1)
    
    elif choice == 3:
        # 'output' output_variable_type list_of_variable_port_identifiers
        result += gen_output_variable_type(depth-1) + " " + gen_list_of_variable_port_identifiers(depth-1)

    return result

# event_declaration
#     : 'event' list_of_event_identifiers ';'
#     ;


def gen_event_declaration(depth=3):
    return "event " + gen_list_of_event_identifiers(depth-1) + ";"


# integer_declaration
#     : 'integer' list_of_variable_identifiers ';'
#     ;

def gen_integer_declaration(depth=3):
    return "integer " + gen_list_of_variable_identifiers(depth-1) + ";"


# net_declaration
#     : net_type 'signed'? delay3? list_of_net_identifiers ';'
#     | net_type drive_strength? 'signed'? delay3? list_of_net_decl_assignments ';'
#     | net_type ('vectored' | 'scalared')? 'signed'? range_ delay3? list_of_net_identifiers ';'
#     | net_type drive_strength? ('vectored' | 'scalared')? 'signed'? range_ delay3? list_of_net_decl_assignments ';'
#     | 'trireg' charge_strength? 'signed'? delay3? list_of_net_identifiers ';'
#     | 'trireg' drive_strength? 'signed'? delay3? list_of_net_decl_assignments ';'
#     | 'trireg' charge_strength? ('vectored' | 'scalared')? 'signed'? range_ delay3? list_of_net_identifiers ';'
#     | 'trireg' drive_strength? ('vectored' | 'scalared')? 'signed'? range_ delay3? list_of_net_decl_assignments ';'
#     ;

import random

def gen_net_declaration(depth=3):
    result = ""

    if random.choice([True, False]):
        result += "trireg"
        if random.choice([True, False]):
            result += " " + gen_charge_strength(depth-1)
    else:
        result += gen_net_type(depth-1)

    if random.choice([True, False]):
        result += " " + gen_drive_strength(depth-1)

    if random.choice([True, False]):
        result += " " + random.choice(["vectored", "scalared"])

    if random.choice([True, False]):
        result += " signed"

    if random.choice([True, False]):
        result += " " + gen_range_(depth-1)

    if random.choice([True, False]):
        result += " " + gen_delay3(depth-1)

    if random.choice([True, False]):
        result += " " + gen_list_of_net_decl_assignments(depth-1)
    else:
        result += " " + gen_list_of_net_identifiers(depth-1)

    return result + ";"

# real_declaration
#     : 'real' list_of_real_identifiers ';'
#     ;

def gen_real_declaration(depth=3):
    return "real " + gen_list_of_real_identifiers(depth-1) + ";"


# realtime_declaration
#     : 'realtime' list_of_real_identifiers ';'
#     ;

def gen_realtime_declaration(depth=3):
    return "realtime " + gen_list_of_real_identifiers(depth-1) + ";"

# reg_declaration
#     : 'reg' 'signed'? range_? list_of_variable_identifiers ';'
#     ;

import random

def gen_reg_declaration(depth=3):
    result = "reg"

    # 可选生成 signed
    if random.choice([True, False]):
        result += " signed"

    # 可选生成 range_
    if random.choice([True, False]):
        result += " " + gen_range_(depth-1)

    result += " " + gen_list_of_variable_identifiers(depth-1) + ";"
    return result


# time_declaration
#     : 'time' list_of_variable_identifiers ';'
#     ;

def gen_time_declaration(depth=3):
    return "time " + gen_list_of_variable_identifiers(depth-1) + ";"


# net_type
#     : 'supply0'
#     | 'supply1'
#     | 'tri'
#     | 'triand'
#     | 'trior'
#     | 'tri0'
#     | 'tri1'
#     | 'uwire'
#     | 'wire'
#     | 'wand'
#     | 'wor'
#     ;

import random

def gen_net_type(depth=3):
    return random.choice([
        "supply0", "supply1", "tri", "triand", "trior",
        "tri0", "tri1", "uwire", "wire", "wand", "wor"
    ])

# output_variable_type
#     : 'integer'
#     | 'time'
#     ;

import random

def gen_output_variable_type(depth=3):
    return random.choice(["integer", "time"])

# real_type
#     : real_identifier dimension*
#     | real_identifier '=' constant_expression
#     ;

import random

def gen_real_type(depth=3):
    result = gen_real_identifier(depth-1)

    if random.choice([True, False]):
        # 生成 0 个或多个 dimension
        while random.choice([True, False]):
            result += " " + gen_dimension(depth-1)
    else:
        # 生成 `= constant_expression`
        result += " = " + gen_constant_expression(depth-1)

    return result


# variable_type
#     : variable_identifier dimension*
#     | variable_identifier '=' constant_expression
#     ;


import random

def gen_variable_type(depth=3):
    result = gen_variable_identifier(depth-1)

    if random.choice([True, False]):
        # 生成 0 个或多个 dimension
        while random.choice([True, False]):
            result += " " + gen_dimension(depth-1)
    else:
        # 生成 `= constant_expression`
        result += " = " + gen_constant_expression(depth-1)

    return result

# drive_strength
#     : '(' strength0 ',' strength1 ')'
#     | '(' strength1 ',' strength0 ')'
#     | '(' strength0 ',' 'highz1' ')'
#     | '(' strength1 ',' 'highz0' ')'
#     | '(' 'highz0' ',' strength1 ')'
#     | '(' 'highz1' ',' strength0 ')'
#     ;

import random

def gen_drive_strength(depth=3):
    strength0 = gen_strength0(depth-1)
    strength1 = gen_strength1(depth-1)
    highz0 = "highz0"
    highz1 = "highz1"

    choices = [
        f"({strength0}, {strength1})",
        f"({strength1}, {strength0})",
        f"({strength0}, {highz1})",
        f"({strength1}, {highz0})",
        f"({highz0}, {strength1})",
        f"({highz1}, {strength0})"
    ]

    return random.choice(choices)

# strength0
#     : 'supply0'
#     | 'strong0'
#     | 'pull0'
#     | 'weak0'
#     ;

import random

def gen_strength0(depth=3):
    return random.choice(["supply0", "strong0", "pull0", "weak0"])

# strength1
#     : 'supply1'
#     | 'strong1'
#     | 'pull1'
#     | 'weak1'
#     ;

import random

def gen_strength1(depth=3):
    return random.choice(["supply1", "strong1", "pull1", "weak1"])

# charge_strength
#     : '(' 'small' ')'
#     | '(' 'medium' ')'
#     | '(' 'large' ')'
#     ;

import random

def gen_charge_strength(depth=3):
    return random.choice(["(small)", "(medium)", "(large)"])

# delay3
#     : '#' delay_value
#     | '#' '(' mintypmax_expression (',' mintypmax_expression ( ',' mintypmax_expression)?)? ')'
#     ;

import random

def gen_delay3(depth=3):
    if random.choice([True, False]):
        # 生成 `# delay_value`
        return "# " + gen_delay_value(depth-1)
    else:
        # 生成 `# (mintypmax_expression [, mintypmax_expression [, mintypmax_expression]])`
        result = "# (" + gen_mintypmax_expression(depth-1)
        if random.choice([True, False]):
            result += ", " + gen_mintypmax_expression(depth-1)
            if random.choice([True, False]):
                result += ", " + gen_mintypmax_expression(depth-1)
        result += ")"
        return result


# delay2
#     : '#' delay_value
#     | '#' '(' mintypmax_expression ( ',' mintypmax_expression)? ')'
#     ;

import random

def gen_delay2(depth=3):
    if random.choice([True, False]):
        # 生成 `# delay_value`
        return "# " + gen_delay_value(depth-1)
    else:
        # 生成 `# (mintypmax_expression [, mintypmax_expression])`
        result = "# (" + gen_mintypmax_expression(depth-1)
        if random.choice([True, False]):
            result += ", " + gen_mintypmax_expression(depth-1)
        result += ")"
        return result

# delay_value
#     : unsigned_number
#     | real_number
#     | identifier
#     ;

import random

def gen_delay_value(depth=3):
    return random.choice([gen_unsigned_number(depth-1), gen_real_number(depth-1), gen_identifier(depth-1)])

# list_of_defparam_assignments
#     : defparam_assignment (',' defparam_assignment)*
#     ;

import random

def gen_list_of_defparam_assignments(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 defparam_assignment
    return ", ".join(gen_defparam_assignment(depth-1) for _ in range(count))

# list_of_event_identifiers
#     : event_id (',' event_id)*
#     ;

import random

def gen_list_of_event_identifiers(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 event_id
    return ", ".join(gen_event_id(depth-1) for _ in range(count))

# event_id
#     : event_identifier dimension*
#     ;

import random

def gen_event_id(depth=3):
    result = gen_event_identifier(depth-1)

    # 生成 0 个或多个 dimension
    while random.choice([True, False]):
        result += " " + gen_dimension(depth-1)

    return result


# list_of_net_decl_assignments
#     : net_decl_assignment (',' net_decl_assignment)*
#     ;

import random

def gen_list_of_net_decl_assignments(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 net_decl_assignment
    return ", ".join(gen_net_decl_assignment(depth-1) for _ in range(count))

# list_of_net_identifiers
#     : net_id (',' net_id)*
#     ;

import random

def gen_list_of_net_identifiers(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 net_id
    return ", ".join(gen_net_id(depth-1) for _ in range(count))

# net_id
#     : net_identifier dimension*
#     ;

import random

def gen_net_id(depth=3):
    result = gen_net_identifier(depth-1)

    # 生成 0 个或多个 dimension
    while random.choice([True, False]):
        result += " " + gen_dimension(depth-1)

    return result


# list_of_param_assignments
#     : param_assignment (',' param_assignment)*
#     ;

import random

def gen_list_of_param_assignments(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 param_assignment
    return ", ".join(gen_param_assignment(depth-1) for _ in range(count))


# list_of_port_identifiers
#     : port_identifier (',' port_identifier)*
#     ;


import random

def gen_list_of_port_identifiers(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 port_identifier
    return ", ".join(gen_port_identifier(depth-1) for _ in range(count))

# list_of_real_identifiers
#     : real_type (',' real_type)*
#     ;

import random

def gen_list_of_real_identifiers(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 real_type
    return ", ".join(gen_real_type(depth-1) for _ in range(count))

# list_of_specparam_assignments
#     : specparam_assignment (',' specparam_assignment)*
#     ;

import random

def gen_list_of_specparam_assignments(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 specparam_assignment
    return ", ".join(gen_specparam_assignment(depth-1) for _ in range(count))

# list_of_variable_identifiers
#     : variable_type (',' variable_type)*
#     ;

import random

def gen_list_of_variable_identifiers(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 variable_type
    return ", ".join(gen_variable_type(depth-1) for _ in range(count))

# list_of_variable_port_identifiers
#     : var_port_id (',' var_port_id)*
#     ;

import random

def gen_list_of_variable_port_identifiers(depth=3):
    count = random.randint(1, 5)  # 生成 1 到 5 个 var_port_id
    return ", ".join(gen_var_port_id(depth-1) for _ in range(count))


# var_port_id
#     : port_identifier ('=' constant_expression)?
#     ;

import random

def gen_var_port_id(depth=3):
    result = gen_port_identifier(depth-1)

    # 50% 的概率生成可选的 '= constant_expression'
    if random.choice([True, False]):
        result += " = " + gen_constant_expression(depth-1)

    return result

# defparam_assignment
#     : hierarchical_identifier '=' constant_mintypmax_expression
#     ;

def gen_defparam_assignment(depth=3):
    return f"{gen_hierarchical_identifier(depth-1)} = {gen_constant_mintypmax_expression(depth-1)}"


# net_decl_assignment
#     : net_identifier '=' expression
#     ;

def gen_net_decl_assignment(depth=3):
    return f"{gen_net_identifier(depth-1)} = {gen_expression(depth-1)}"

# param_assignment
#     : parameter_identifier '=' constant_mintypmax_expression
#     ;

def gen_param_assignment(depth=3):
    return f"{gen_parameter_identifier(depth-1)} = {gen_constant_mintypmax_expression(depth-1)}"

# specparam_assignment
#     : specparam_identifier '=' constant_mintypmax_expression
#     | pulse_control_specparam
#     ;

import random

def gen_specparam_assignment(depth=3):
    if random.choice([True, False]):
        return f"{gen_specparam_identifier(depth-1)} = {gen_constant_mintypmax_expression(depth-1)}"
    else:
        return gen_pulse_control_specparam(depth-1)



# pulse_control_specparam
#     : 'PATHPULSE$' '=' '(' reject_limit_value (',' error_limit_value)? ')'
#     | 'PATHPULSE$' specify_input_terminal_descriptor '$' specify_output_terminal_descriptor '=' '(' reject_limit_value (
#         ',' error_limit_value
#     )? ')'
#     ;

import random

def gen_pulse_control_specparam(depth=3):
    if random.choice([True, False]):
        # 生成 "PATHPULSE$ = (reject_limit_value [, error_limit_value])"
        result = f"PATHPULSE$ = ({gen_reject_limit_value(depth-1)}"
        if random.choice([True, False]):  # 50% 概率生成可选的 error_limit_value
            result += f", {gen_error_limit_value(depth-1)}"
        result += ")"
    else:
        # 生成 "PATHPULSE$ specify_input_terminal_descriptor $ specify_output_terminal_descriptor = (reject_limit_value [, error_limit_value])"
        result = f"PATHPULSE$ {gen_specify_input_terminal_descriptor(depth-1)} $ {gen_specify_output_terminal_descriptor(depth-1)} = ({gen_reject_limit_value(depth-1)}"
        if random.choice([True, False]):  # 50% 概率生成可选的 error_limit_value
            result += f", {gen_error_limit_value(depth-1)}"
        result += ")"
    
    return result

# error_limit_value
#     : limit_value
#     ;

def gen_error_limit_value(depth=3):
    return gen_limit_value(depth-1)


# reject_limit_value
#     : limit_value
#     ;

def gen_reject_limit_value(depth=3):
    return gen_limit_value(depth-1)

# limit_value
#     : constant_mintypmax_expression

def gen_limit_value(depth=3):
    return gen_constant_mintypmax_expression(depth-1)

# dimension
#     : '[' dimension_constant_expression ':' dimension_constant_expression ']'
#     ;

def gen_dimension(depth=3):
    return f"[{gen_dimension_constant_expression(depth-1)} : {gen_dimension_constant_expression(depth-1)}]"

# range_
#     : '[' msb_constant_expression ':' lsb_constant_expression ']'
#     ;

def gen_range_(depth=3):
    return f"[{gen_msb_constant_expression(depth-1)} : {gen_lsb_constant_expression(depth-1)}]"

# function_declaration
#     : 'function' 'automatic'? function_range_or_type? function_identifier ';' function_item_declaration+ function_statement 'endfunction'
#     | 'function' 'automatic'? function_range_or_type? function_identifier '(' function_port_list ')' ';' block_item_declaration* function_statement
#         'endfunction'
#     ;

import random

def gen_function_declaration(depth=3):
    result = "function"
    
    # 50% 概率添加 'automatic'
    if random.choice([True, False]):
        result += " automatic"

    # 50% 概率添加 function_range_or_type
    if random.choice([True, False]):
        result += f" {gen_function_range_or_type(depth-1)}"

    result += f" {gen_function_identifier(depth-1)}"

    if random.choice([True, False]):  # 50% 概率生成带参数的 function
        result += f"({gen_function_port_list(depth-1)})"

    result += ";\n"

    # 50% 概率生成 function_item_declaration 或 block_item_declaration
    if random.choice([True, False]):
        result += "\n".join(gen_function_item_declaration(depth-1) for _ in range(random.randint(1, 3)))
    else:
        result += "\n".join(gen_block_item_declaration(depth-1) for _ in range(random.randint(0, 3)))

    result += f"\n{gen_function_statement(depth-1)}\nendfunction"

    return result

# function_item_declaration
#     : block_item_declaration
#     | attribute_instance* tf_input_declaration ';'
#     ;

import random

def gen_function_item_declaration(depth=3):
    if random.choice([True, False]):
        return gen_block_item_declaration(depth-1)
    else:
        attr = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 2)))  # 生成 0~2 个 attribute_instance
        return f"{attr} {gen_tf_input_declaration(depth-1)};".strip()

# function_port_list
#     : func_port_item (',' func_port_item)*
#     ;

import random

def gen_function_port_list(depth=3):
    num_ports = random.randint(1, 4)  # 随机生成 1 到 4 个端口
    return ", ".join(gen_func_port_item(depth-1) for _ in range(num_ports))

# func_port_item
#     : attribute_instance* tf_input_declaration
#     ;

import random

def gen_func_port_item(depth=3):
    attr = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 2)))  # 生成 0~2 个 attribute_instance
    return f"{attr} {gen_tf_input_declaration(depth-1)}".strip()

# function_range_or_type
#     : range_
#     | 'signed' range_?
#     | 'integer'
#     | 'real'
#     | 'realtime'
#     | 'time'
#     ;

import random

def gen_function_range_or_type(depth=3):
    options = [
        gen_range_(depth-1), 
        f"signed {gen_range_(depth-1)}" if random.choice([True, False]) else "signed",
        "integer",
        "real",
        "realtime",
        "time"
    ]
    return random.choice(options)


# task_declaration
#     : 'task' 'automatic'? task_identifier ';' task_item_declaration* statement_or_null 'endtask'
#     | 'task' 'automatic'? task_identifier '(' task_port_list? ')' ';' block_item_declaration* statement_or_null 'endtask'
#     ;

import random

def gen_task_declaration(depth=3):
    result = "task"

    # 50% 概率添加 'automatic'
    if random.choice([True, False]):
        result += " automatic"

    result += f" {gen_task_identifier(depth-1)}"

    if random.choice([True, False]):  # 50% 概率生成带参数的 task
        result += f"({gen_task_port_list(depth-1)})" if random.choice([True, False]) else "(depth-1)"

    result += ";\n"

    # 50% 概率生成 task_item_declaration 或 block_item_declaration
    if random.choice([True, False]):
        result += "\n".join(gen_task_item_declaration(depth-1) for _ in range(random.randint(0, 3)))
    else:
        result += "\n".join(gen_block_item_declaration(depth-1) for _ in range(random.randint(0, 3)))

    result += f"\n{gen_statement_or_null(depth-1)}\nendtask"

    return result

# task_item_declaration
#     : block_item_declaration
#     | attribute_instance* tf_input_declaration ';'
#     | attribute_instance* tf_output_declaration ';'
#     | attribute_instance* tf_inout_declaration ';'
#     ;

import random

def gen_task_item_declaration(depth=3):
    choice = random.choice(["block", "input", "output", "inout"])

    if choice == "block":
        return gen_block_item_declaration(depth-1)
    
    attr = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 2)))  # 生成 0~2 个 attribute_instance

    if choice == "input":
        decl = gen_tf_input_declaration(depth-1)
    elif choice == "output":
        decl = gen_tf_output_declaration(depth-1)
    else:  # choice == "inout"
        decl = gen_tf_inout_declaration(depth-1)

    return f"{attr} {decl};".strip()

# task_port_list
#     : task_port_item (',' task_port_item)*
#     ;

import random

def gen_task_port_list(depth=3):
    num_ports = random.randint(1, 4)  # 随机生成 1 到 4 个端口
    return ", ".join(gen_task_port_item(depth-1) for _ in range(num_ports))


# task_port_item
#     : attribute_instance* tf_input_declaration
#     | attribute_instance* tf_output_declaration
#     | attribute_instance* tf_inout_declaration
#     ;

import random

def gen_task_port_item(depth=3):
    attr = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 2)))  # 生成 0~2 个 attribute_instance

    choice = random.choice(["input", "output", "inout"])
    if choice == "input":
        decl = gen_tf_input_declaration(depth-1)
    elif choice == "output":
        decl = gen_tf_output_declaration(depth-1)
    else:  # choice == "inout"
        decl = gen_tf_inout_declaration(depth-1)

    return f"{attr} {decl}".strip()

# tf_input_declaration
#     : 'input' 'reg'? 'signed'? range_? list_of_port_identifiers
#     | 'input' task_port_type list_of_port_identifiers
#     ;

import random

def gen_tf_input_declaration(depth=3):
    result = "input"

    if random.choice([True, False]):  # 50% 概率添加 'reg'
        result += " reg"

    if random.choice([True, False]):  # 50% 概率添加 'signed'
        result += " signed"

    if random.choice([True, False]):  # 50% 概率包含 range_
        result += f" {gen_range_(depth-1)}"

    result += f" {gen_list_of_port_identifiers(depth-1)}" if random.choice([True, False]) else f" {gen_task_port_type(depth-1)} {gen_list_of_port_identifiers(depth-1)}"

    return result

# tf_output_declaration
#     : 'output' 'reg'? 'signed'? range_? list_of_port_identifiers
#     | 'output' task_port_type list_of_port_identifiers
#     ;


import random

def gen_tf_output_declaration(depth=3):
    result = "output"

    if random.choice([True, False]):  # 50% 概率添加 'reg'
        result += " reg"

    if random.choice([True, False]):  # 50% 概率添加 'signed'
        result += " signed"

    if random.choice([True, False]):  # 50% 概率包含 range_
        result += f" {gen_range_(depth-1)}"

    result += f" {gen_list_of_port_identifiers(depth-1)}" if random.choice([True, False]) else f" {gen_task_port_type(depth-1)} {gen_list_of_port_identifiers(depth-1)}"

    return result


# tf_inout_declaration
#     : 'inout' 'reg'? 'signed'? range_? list_of_port_identifiers
#     | 'inout' task_port_type list_of_port_identifiers
#     ;

import random

def gen_tf_inout_declaration(depth=3):
    result = "inout"

    if random.choice([True, False]):  # 50% 概率添加 'reg'
        result += " reg"

    if random.choice([True, False]):  # 50% 概率添加 'signed'
        result += " signed"

    if random.choice([True, False]):  # 50% 概率包含 range_
        result += f" {gen_range_(depth-1)}"

    result += f" {gen_list_of_port_identifiers(depth-1)}" if random.choice([True, False]) else f" {gen_task_port_type(depth-1)} {gen_list_of_port_identifiers(depth-1)}"

    return result


# task_port_type
#     : 'integer'
#     | 'real'
#     | 'realtime'
#     | 'time'
#     ;

import random

def gen_task_port_type(depth=3):
    return random.choice(["integer", "real", "realtime", "time"])

# block_item_declaration
#     : attribute_instance* 'reg' 'signed'? range_? list_of_block_variable_identifiers ';'
#     | attribute_instance* 'integer' list_of_block_variable_identifiers ';'
#     | attribute_instance* 'time' list_of_block_variable_identifiers ';'
#     | attribute_instance* 'real' list_of_block_real_identifiers ';'
#     | attribute_instance* 'realtime' list_of_block_real_identifiers ';'
#     | attribute_instance* event_declaration
#     | attribute_instance* local_parameter_declaration ';'
#     | attribute_instance* parameter_declaration ';'
#     ;

import random

def gen_block_item_declaration(depth=3):
    result = ""

    # 可能包含 attribute_instance*，这里假设 attribute_instance 生成函数已实现
    if random.choice([True, False]):  
        result += f"{gen_attribute_instance(depth-1)} "

    choice = random.randint(1, 8)

    if choice == 1:
        result += "reg"
        if random.choice([True, False]):
            result += " signed"
        if random.choice([True, False]):
            result += f" {gen_range_(depth-1)}"
        result += f" {gen_list_of_block_variable_identifiers(depth-1)};"

    elif choice == 2:
        result += f"integer {gen_list_of_block_variable_identifiers(depth-1)};"

    elif choice == 3:
        result += f"time {gen_list_of_block_variable_identifiers(depth-1)};"

    elif choice == 4:
        result += f"real {gen_list_of_block_real_identifiers(depth-1)};"

    elif choice == 5:
        result += f"realtime {gen_list_of_block_real_identifiers(depth-1)};"

    elif choice == 6:
        result += gen_event_declaration(depth-1)  # 假设 event_declaration 生成函数已实现

    elif choice == 7:
        result += f"{gen_local_parameter_declaration(depth-1)};"

    elif choice == 8:
        result += f"{gen_parameter_declaration(depth-1)};"

    return result

# list_of_block_variable_identifiers
#     : block_variable_type (',' block_variable_type)*
#     ;

import random

def gen_list_of_block_variable_identifiers(depth=3):
    count = random.randint(1, 5)  # 随机生成 1 到 5 个 block_variable_type
    return ", ".join(gen_block_variable_type(depth-1) for _ in range(count))

# 假设 gen_block_variable_type(depth-1) 已经实现


# list_of_block_real_identifiers
#     : block_real_type (',' block_real_type)*
#     ;

import random

def gen_list_of_block_real_identifiers(depth=3):
    count = random.randint(1, 5)  # 随机生成 1 到 5 个 block_real_type
    return ", ".join(gen_block_real_type(depth-1) for _ in range(count))

# 假设 gen_block_real_type(depth-1) 已经实现


# block_variable_type
#     : variable_identifier dimension*
#     ;


import random

def gen_block_variable_type(depth=3):
    var_id = gen_variable_identifier(depth-1)  # 生成 variable_identifier
    if random.choice([True, False]):  # 随机决定是否添加 dimension
        dimensions = " ".join(gen_dimension(depth-1) for _ in range(random.randint(1, 3)))  # 随机生成 1 到 3 个维度
        return f"{var_id} {dimensions}"
    return var_id

# 假设 gen_variable_identifier(depth-1) 和 gen_dimension(depth-1) 已经实现

# block_real_type
#     : real_identifier dimension*
#     ;

import random

def gen_block_real_type(depth=3):
    real_id = gen_real_identifier(depth-1)  # 生成 real_identifier
    if random.choice([True, False]):  # 随机决定是否添加 dimension
        dimensions = " ".join(gen_dimension(depth-1) for _ in range(random.randint(1, 3)))  # 随机生成 1 到 3 个维度
        return f"{real_id} {dimensions}"
    return real_id

# 假设 gen_real_identifier(depth-1) 和 gen_dimension(depth-1) 已经实现


# gate_instantiation
#     : cmos_switchtype delay3? cmos_switch_instance (',' cmos_switch_instance)* ';'
#     | enable_gatetype drive_strength? delay3? enable_gate_instance (',' enable_gate_instance)* ';'
#     | mos_switchtype delay3? mos_switch_instance ( ',' mos_switch_instance)* ';'
#     | n_input_gatetype drive_strength? delay2? n_input_gate_instance (',' n_input_gate_instance)* ';'
#     | n_output_gatetype drive_strength? delay2? n_output_gate_instance (',' n_output_gate_instance)* ';'
#     | pass_en_switchtype delay2? pass_enable_switch_instance (',' pass_enable_switch_instance)* ';'
#     | pass_switchtype pass_switch_instance ( ',' pass_switch_instance)* ';'
#     | 'pulldown' pulldown_strength? pull_gate_instance (',' pull_gate_instance)* ';'
#     | 'pullup' pullup_strength? pull_gate_instance ( ',' pull_gate_instance)* ';'
#     ;


import random

def gen_gate_instantiation(depth=3):
    choices = [
        lambda: f"{gen_cmos_switchtype(depth-1)} {gen_optional_delay3(depth-1)} {gen_comma_separated_instances(gen_cmos_switch_instance)};",
        lambda: f"{gen_enable_gatetype(depth-1)} {gen_optional_drive_strength(depth-1)} {gen_optional_delay3(depth-1)} {gen_comma_separated_instances(gen_enable_gate_instance)};",
        lambda: f"{gen_mos_switchtype(depth-1)} {gen_optional_delay3(depth-1)} {gen_comma_separated_instances(gen_mos_switch_instance)};",
        lambda: f"{gen_n_input_gatetype(depth-1)} {gen_optional_drive_strength(depth-1)} {gen_optional_delay2(depth-1)} {gen_comma_separated_instances(gen_n_input_gate_instance)};",
        lambda: f"{gen_n_output_gatetype(depth-1)} {gen_optional_drive_strength(depth-1)} {gen_optional_delay2(depth-1)} {gen_comma_separated_instances(gen_n_output_gate_instance)};",
        lambda: f"{gen_pass_en_switchtype(depth-1)} {gen_optional_delay2(depth-1)} {gen_comma_separated_instances(gen_pass_enable_switch_instance)};",
        lambda: f"{gen_pass_switchtype(depth-1)} {gen_comma_separated_instances(gen_pass_switch_instance)};",
        lambda: f"pulldown {gen_optional_pulldown_strength(depth-1)} {gen_comma_separated_instances(gen_pull_gate_instance)};",
        lambda: f"pullup {gen_optional_pullup_strength(depth-1)} {gen_comma_separated_instances(gen_pull_gate_instance)};"
    ]
    return random.choice(choices)()

def gen_optional_delay3(depth=3):
    return gen_delay3(depth-1) if random.choice([True, False]) else ""

def gen_optional_delay2(depth=3):
    return gen_delay2(depth-1) if random.choice([True, False]) else ""

def gen_optional_drive_strength(depth=3):
    return gen_drive_strength(depth-1) if random.choice([True, False]) else ""

def gen_optional_pulldown_strength(depth=3):
    return gen_pulldown_strength(depth-1) if random.choice([True, False]) else ""

def gen_optional_pullup_strength(depth=3):
    return gen_pullup_strength(depth-1) if random.choice([True, False]) else ""


import random

def gen_comma_separated_instances(instance_gen):
    count = random.randint(1, 3)  # 生成 1 到 3 个实例
    return ", ".join(instance_gen() for _ in range(count))

# 假设 gen_cmos_switchtype(depth-1), gen_delay3(depth-1), gen_cmos_switch_instance(depth-1) 等已实现


# cmos_switch_instance
#     : name_of_gate_instance? '(' output_terminal ',' input_terminal ',' ncontrol_terminal ',' pcontrol_terminal ')'
#     ;


import random

def gen_cmos_switch_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    result += gen_output_terminal(depth-1) + ", "
    result += gen_input_terminal(depth-1) + ", "
    result += gen_ncontrol_terminal(depth-1) + ", "
    result += gen_pcontrol_terminal(depth-1)
    result += ")"
    return result


# enable_gate_instance
#     : name_of_gate_instance? '(' output_terminal ',' input_terminal ',' enable_terminal ')'
#     ;

import random

def gen_enable_gate_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    result += gen_output_terminal(depth-1) + ", "
    result += gen_input_terminal(depth-1) + ", "
    result += gen_enable_terminal(depth-1)
    result += ")"
    return result


# mos_switch_instance
#     : name_of_gate_instance? '(' output_terminal ',' input_terminal ',' enable_terminal ')'
#     ;


import random

def gen_mos_switch_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    result += gen_output_terminal(depth-1) + ", "
    result += gen_input_terminal(depth-1) + ", "
    result += gen_enable_terminal(depth-1)
    result += ")"
    return result


# n_input_gate_instance
#     : name_of_gate_instance? '(' output_terminal ',' input_terminal (',' input_terminal)* ')'
#     ;

import random

def gen_n_input_gate_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    result += gen_output_terminal(depth-1) + ", "
    result += gen_input_terminal(depth-1)
    # 可选生成额外的 input_terminal
    for _ in range(random.randint(0, 3)):
        result += ", " + gen_input_terminal(depth-1)
    result += ")"
    return result


# n_output_gate_instance
#     : name_of_gate_instance? '(' output_terminal (',' output_terminal)* ',' input_terminal ')'
#     ;

import random

def gen_n_output_gate_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    # 必须生成至少一个 output_terminal
    result += gen_output_terminal(depth-1)
    # 随机生成额外的 output_terminal，数量可为 0 到 3 个
    for _ in range(random.randint(0, 3)):
        result += ", " + gen_output_terminal(depth-1)
    # 最后添加一个 input_terminal，前面需要添加逗号分隔
    result += ", " + gen_input_terminal(depth-1)
    result += ")"
    return result

# pass_switch_instance
#     : name_of_gate_instance? '(' inout_terminal ',' inout_terminal ')'
#     ;


import random

def gen_pass_switch_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    result += gen_inout_terminal(depth-1) + ", " + gen_inout_terminal(depth-1)
    result += ")"
    return result


# pass_enable_switch_instance
#     : name_of_gate_instance? '(' inout_terminal ',' inout_terminal ',' enable_terminal ')'
#     ;

import random

def gen_pass_enable_switch_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "("
    result += gen_inout_terminal(depth-1) + ", " + gen_inout_terminal(depth-1) + ", " + gen_enable_terminal(depth-1)
    result += ")"
    return result

# pull_gate_instance
#     : name_of_gate_instance? '(' output_terminal ')'
#     ;

import random

def gen_pull_gate_instance(depth=3):
    result = ""
    # 可选生成 name_of_gate_instance
    if random.choice([True, False]):
        result += gen_name_of_gate_instance(depth-1) + " "
    result += "(" + gen_output_terminal(depth-1) + ")"
    return result


# name_of_gate_instance
#     : gate_instance_identifier range_?
#     ;

import random

def gen_name_of_gate_instance(depth=3):
    result = gen_gate_instance_identifier(depth-1)
    if random.choice([True, False]):
        result += " " + gen_range_(depth-1)
    return result


# pulldown_strength
#     : '(' strength0 ',' strength1 ')'
#     | '(' strength1 ',' strength0 ')'
#     | '(' strength0 ')'
#     ;

import random

def gen_pulldown_strength(depth=3):
    option = random.randint(1, 3)
    if option == 1:
        return f"({gen_strength0(depth-1)}, {gen_strength1(depth-1)})"
    elif option == 2:
        return f"({gen_strength1(depth-1)}, {gen_strength0(depth-1)})"
    else:  # option == 3
        return f"({gen_strength0(depth-1)})"

# pullup_strength
#     : '(' strength0 ',' strength1 ')'
#     | '(' strength1 ',' strength0 ')'
#     | '(' strength1 ')'
#     ;


import random

def gen_pullup_strength(depth=3):
    option = random.randint(1, 3)
    if option == 1:
        return f"({gen_strength0(depth-1)}, {gen_strength1(depth-1)})"
    elif option == 2:
        return f"({gen_strength1(depth-1)}, {gen_strength0(depth-1)})"
    else:  # option == 3
        return f"({gen_strength1(depth-1)})"

# enable_terminal
#     : expression
#     ;

def gen_enable_terminal(depth=3):
    return gen_expression(depth-1)


# inout_terminal
#     : net_lvalue
#     ;

def gen_inout_terminal(depth=3):
    return gen_net_lvalue(depth-1)

# input_terminal
#     : expression
#     ;


def gen_input_terminal(depth=3):
    return gen_expression(depth-1)


# ncontrol_terminal
#     : expression
#     ;

def gen_ncontrol_terminal(depth=3):
    return gen_expression(depth-1)


# output_terminal
#     : net_lvalue
#     ;

def gen_output_terminal(depth=3):
    return gen_net_lvalue(depth-1)


# pcontrol_terminal
#     : expression
#     ;

def gen_pcontrol_terminal(depth=3):
    return gen_expression(depth-1)


# cmos_switchtype
#     : 'cmos'
#     | 'rcmos'
#     ;

import random

def gen_cmos_switchtype(depth=3):
    return random.choice(["cmos", "rcmos"])


# enable_gatetype
#     : 'bufif0'
#     | 'bufif1'
#     | 'notif0'
#     | 'notif1'
#     ;

import random

def gen_enable_gatetype(depth=3):
    return random.choice(["bufif0", "bufif1", "notif0", "notif1"])


# mos_switchtype
#     : 'nmos'
#     | 'pmos'
#     | 'rnmos'
#     | 'rpmos'
#     ;

import random

def gen_mos_switchtype(depth=3):
    return random.choice(["nmos", "pmos", "rnmos", "rpmos"])

# n_input_gatetype
#     : 'and'
#     | 'nand'
#     | 'or'
#     | 'nor'
#     | 'xor'
#     | 'xnor'
#     ;

import random

def gen_n_input_gatetype(depth=3):
    return random.choice(["and", "nand", "or", "nor", "xor", "xnor"])


# n_output_gatetype
#     : 'buf'
#     | 'not'
#     ;

import random

def gen_n_output_gatetype(depth=3):
    return random.choice(["buf", "not"])


# pass_en_switchtype
#     : 'tranif0'
#     | 'tranif1'
#     | 'rtranif1'
#     | 'rtranif0'
#     ;

import random

def gen_pass_en_switchtype(depth=3):
    return random.choice(["tranif0", "tranif1", "rtranif1", "rtranif0"])


# pass_switchtype
#     : 'tran'
#     | 'rtran'
#     ;

def gen_pass_switchtype(depth=3):
    return random.choice(["tran", "rtran"])


# module_instantiation
#     : module_identifier parameter_value_assignment? module_instance (',' module_instance)* ';'
#     ;

def gen_module_instantiation(depth=3):
    module_identifier = gen_module_identifier(depth-1)
    parameter_value_assignment = gen_parameter_value_assignment(depth-1) if random.choice([True, False]) else ""
    module_instances = [gen_module_instance(depth-1) for _ in range(random.randint(1, 3))]
    return f"{module_identifier} {parameter_value_assignment} {', '.join(module_instances)};"

# parameter_value_assignment
#     : '#' '(' list_of_parameter_assignments ')'
#     ;

def gen_parameter_value_assignment(depth=3):
    list_of_parameter_assignments = gen_list_of_parameter_assignments(depth-1)
    return f"#({list_of_parameter_assignments})"

# list_of_parameter_assignments
#     : ordered_parameter_assignment (',' ordered_parameter_assignment)*
#     | named_parameter_assignment ( ',' named_parameter_assignment)*
#     ;


def gen_list_of_parameter_assignments(depth=3):
    import random

    if random.choice([True, False]):  # 随机选择使用有序或命名参数
        assignments = [gen_ordered_parameter_assignment(depth-1) for _ in range(random.randint(1, 3))]
    else:
        assignments = [gen_named_parameter_assignment(depth-1) for _ in range(random.randint(1, 3))]
    
    return ", ".join(assignments)

# ordered_parameter_assignment
#     : expression
#     ;

def gen_ordered_parameter_assignment(depth=3):
    return gen_expression(depth-1)

# named_parameter_assignment
#     : '.' parameter_identifier '(' mintypmax_expression? ')'
#     ;

def gen_named_parameter_assignment(depth=3):
    param_id = gen_parameter_identifier(depth-1)
    expr = gen_mintypmax_expression(depth-1) if random.choice([True, False]) else ""
    return f".{param_id}({expr})"


# module_instance
#     : name_of_module_instance '(' list_of_port_connections ')'
#     ;

def gen_module_instance(depth=3):
    name = gen_name_of_module_instance(depth-1)
    ports = gen_list_of_port_connections(depth-1)
    return f"{name}({ports})"


# name_of_module_instance
#     : module_instance_identifier range_?
#     ;


def gen_name_of_module_instance(depth=3):
    name = gen_module_instance_identifier(depth-1)
    if random.choice([True, False]):  # 随机决定是否包含 range_
        name += gen_range_(depth-1)
    return name


# list_of_port_connections
#     : ordered_port_connection (',' ordered_port_connection)*
#     | named_port_connection ( ',' named_port_connection)*
#     ;

def gen_list_of_port_connections(depth=3):
    if random.choice([True, False]):  # 随机选择使用有序或命名端口连接
        connections = [gen_ordered_port_connection(depth-1) for _ in range(random.randint(1, 3))]
    else:
        connections = [gen_named_port_connection(depth-1) for _ in range(random.randint(1, 3))]
    
    return ", ".join(connections)


# ordered_port_connection
#     : attribute_instance* expression?
#     ;

def gen_ordered_port_connection(depth=3):
    """生成符合 ordered_port_connection 规则的字符串"""
    connection = ""
    
    # 可能包含 attribute_instance，但这里简化忽略
    if random.choice([True, False]):  # expression 是可选的
        connection = gen_expression(depth-1)
    
    return connection

# named_port_connection
#     : attribute_instance* '.' port_identifier '(' expression? ')'
#     ;

def gen_named_port_connection(depth=3):
    """生成符合 named_port_connection 规则的字符串"""
    port_id = gen_port_identifier(depth-1)  # 生成端口标识符
    expr = gen_expression(depth-1) if random.choice([True, False]) else ""  # expression 可选
    
    return f".{port_id}({expr})"

# generate_region
#     : 'generate' module_or_generate_item* 'endgenerate'
#     ;

def gen_generate_region(depth=3):
    """生成符合 generate_region 规则的字符串"""
    items = "\n".join(gen_module_or_generate_item(depth-1) for _ in range(random.randint(0, 5)))  
    return f"generate\n{items}\nendgenerate"

# genvar_declaration
#     : 'genvar' list_of_genvar_identifiers ';'
#     ;

def gen_genvar_declaration(depth=3):
    """生成符合 genvar_declaration 规则的字符串"""
    identifiers = ", ".join(gen_list_of_genvar_identifiers(depth-1))  
    return f"genvar {identifiers};"


# list_of_genvar_identifiers
#     : genvar_identifier (',' genvar_identifier)*
#     ;

def gen_list_of_genvar_identifiers(depth=3):
    """生成符合 list_of_genvar_identifiers 规则的字符串"""
    identifiers = [gen_genvar_identifier(depth-1) for _ in range(random.randint(1, 5))]
    return ", ".join(identifiers)


# loop_generate_construct
#     : 'for' '(' genvar_initialization ';' genvar_expression ';' genvar_iteration ')' generate_block
#     ;

def gen_loop_generate_construct(depth=3):
    """生成符合 loop_generate_construct 规则的字符串"""
    initialization = gen_genvar_initialization(depth-1)
    expression = gen_genvar_expression(depth-1)
    iteration = gen_genvar_iteration(depth-1)
    generate_block = gen_generate_block(depth-1)
    
    return f"for ({initialization}; {expression}; {iteration}) {generate_block}"

# genvar_initialization
#     : genvar_identifier '=' constant_expression
#     ;

def gen_genvar_initialization(depth=3):
    """生成符合 genvar_initialization 规则的字符串"""
    genvar_id = gen_genvar_identifier(depth-1)
    const_expr = gen_constant_expression(depth-1)
    
    return f"{genvar_id} = {const_expr}"


# genvar_expression
#     : constant_expression
#     ;

def gen_genvar_expression(depth=3):
    """生成符合 genvar_expression 规则的字符串"""
    return gen_constant_expression(depth-1)


# genvar_iteration
#     : genvar_identifier '=' genvar_expression
#     ;

def gen_genvar_iteration(depth=3):
    """生成符合 genvar_iteration 规则的字符串"""
    return f"{gen_genvar_identifier(depth-1)} = {gen_genvar_expression(depth-1)}"



# conditional_generate_construct
#     : if_generate_construct
#     | case_generate_construct
#     ;

import random

def gen_conditional_generate_construct(depth=3):
    """生成符合 conditional_generate_construct 规则的字符串"""
    if random.choice([True, False]):
        return gen_if_generate_construct(depth-1)
    else:
        return gen_case_generate_construct(depth-1)


# if_generate_construct
#     : 'if' '(' constant_expression ')' generate_block_or_null ('else' generate_block_or_null)?
#     ;

import random

def gen_if_generate_construct(depth=3):
    """生成符合 if_generate_construct 规则的字符串"""
    if_block = f"if ({gen_constant_expression(depth-1)}) {gen_generate_block_or_null(depth-1)}"
    if random.choice([True, False]):  # 随机决定是否生成 else 分支
        if_block += f" else {gen_generate_block_or_null(depth-1)}"
    return if_block



# case_generate_construct
#     : 'case' '(' constant_expression ')' case_generate_item+ 'endcase'
#     ;

import random

def gen_case_generate_construct(depth=3):
    """生成符合 case_generate_construct 规则的字符串"""
    case_expr = gen_constant_expression(depth-1)
    num_items = random.randint(1, 4)  # 生成 1 到 4 个 case 选项
    case_items = "\n".join(gen_case_generate_item(depth-1) for _ in range(num_items))
    
    return f"case ({case_expr})\n{case_items}\nendcase"



# case_generate_item
#     : constant_expression (',' constant_expression)* ':' generate_block_or_null
#     | 'default' ':'? generate_block_or_null
#     ;

import random

def gen_case_generate_item(depth=3):
    """生成符合 case_generate_item 规则的字符串"""
    if random.choice([True, False]):  
        # 生成带 constant_expression 的 case 分支
        num_expr = random.randint(1, 3)  # 1 到 3 个 constant_expression
        expr_list = ", ".join(gen_constant_expression(depth-1) for _ in range(num_expr))
        return f"{expr_list} : {gen_generate_block_or_null(depth-1)}"
    else:
        # 生成 default 分支
        return f"default: {gen_generate_block_or_null(depth-1)}"


# generate_block
#     : module_or_generate_item
#     | 'begin' generate_block_name? module_or_generate_item* 'end'
#     ;

import random

def gen_generate_block(depth=3):
    """生成符合 generate_block 规则的字符串"""
    if random.choice([True, False]):  
        # 直接生成单个 module_or_generate_item
        return gen_module_or_generate_item(depth-1)
    else:
        # 生成 begin...end 块
        block_name = gen_generate_block_name(depth-1) if random.choice([True, False]) else ""
        items = "\n    ".join(gen_module_or_generate_item(depth-1) for _ in range(random.randint(1, 3)))
        return f"begin {block_name}\n    {items}\nend"


# generate_block_name
#     : ':' generate_block_identifier
#     ;

def gen_generate_block_name(depth=3):
    """生成符合 generate_block_name 规则的字符串"""
    return f": {gen_generate_block_identifier(depth-1)}"


# generate_block_or_null
#     : generate_block
#     | ';'
#     ;

import random

def gen_generate_block_or_null(depth=3):
    """生成符合 generate_block_or_null 规则的字符串"""
    if random.choice([True, False]):
        return gen_generate_block(depth-1)
    return ";"



# udp_declaration
#     : attribute_instance* 'primitive' udp_identifier '(' udp_port_list ')' ';' udp_port_declaration+ udp_body 'endprimitive'
#     | attribute_instance* 'primitive' udp_identifier '(' udp_declaration_port_list ')' ';' udp_body 'endprimitive'
#     ;

import random

def gen_udp_declaration(depth=3):
    """生成符合 udp_declaration 规则的字符串"""
    udp_id = gen_udp_identifier(depth-1)
    ports = gen_udp_port_list(depth-1) if random.choice([True, False]) else gen_udp_declaration_port_list(depth-1)
    body = gen_udp_body(depth-1)
    
    return f"primitive {udp_id} ({ports});\n{body}\nendprimitive"


# udp_port_list
#     : output_port_identifier ',' input_port_identifier (',' input_port_identifier)*
#     ;


import random

def gen_udp_port_list(depth=3):
    """生成符合 udp_port_list 规则的字符串"""
    output_port = gen_output_port_identifier(depth-1)
    input_ports = [gen_input_port_identifier(depth-1) for _ in range(random.randint(1, 3))]
    
    return f"{output_port}, {', '.join(input_ports)}"



# udp_declaration_port_list
#     : udp_output_declaration ',' udp_input_declaration (',' udp_input_declaration)*
#     ;

import random

def gen_udp_declaration_port_list(depth=3):
    """生成符合 udp_declaration_port_list 规则的字符串"""
    output_port = gen_udp_output_declaration(depth-1)
    input_ports = [gen_udp_input_declaration(depth-1) for _ in range(random.randint(1, 3))]
    
    return f"{output_port}, {', '.join(input_ports)}"



# udp_port_declaration
#     : udp_output_declaration ';'
#     | udp_input_declaration ';'
#     | udp_reg_declaration ';'
#     ;

import random

def gen_udp_port_declaration(depth=3):
    """生成符合 udp_port_declaration 规则的字符串"""
    choice = random.choice(["output", "input", "reg"])
    
    if choice == "output":
        return gen_udp_output_declaration(depth-1) + ";"
    elif choice == "input":
        return gen_udp_input_declaration(depth-1) + ";"
    else:
        return gen_udp_reg_declaration(depth-1) + ";"



# udp_output_declaration
#     : attribute_instance* 'output' port_identifier
#     | attribute_instance* 'output' 'reg' port_identifier ('=' constant_expression)?
#     ;

import random

def gen_udp_output_declaration(depth=3):
    """生成符合 udp_output_declaration 规则的字符串"""
    output_decl = "output "  # 必须以 'output' 开头
    
    if random.choice([True, False]):  # 50% 概率添加 'reg'
        output_decl += "reg "
    
    output_decl += gen_port_identifier(depth-1)  # 生成端口标识符
    
    if "reg" in output_decl and random.choice([True, False]):  # 如果是 'output reg'，50% 概率生成初始化值
        output_decl += " = " + gen_constant_expression(depth-1)
    
    return output_decl


# udp_input_declaration
#     : attribute_instance* 'input' list_of_port_identifiers
#     ;


import random

def gen_udp_input_declaration(depth=3):
    """生成符合 udp_input_declaration 规则的字符串"""
    input_decl = "input "  # 以 'input' 开头
    
    input_decl += gen_list_of_port_identifiers(depth-1)  # 生成端口标识符列表
    
    return input_decl


# udp_reg_declaration
#     : attribute_instance* 'reg' variable_identifier
#     ;

import random

def gen_udp_reg_declaration(depth=3):
    """生成符合 udp_reg_declaration 规则的字符串"""
    return f"reg {gen_variable_identifier(depth-1)}"


# udp_body
#     : combinational_body
#     | sequential_body
#     ;

import random

def gen_udp_body(depth=3):
    """生成符合 udp_body 规则的字符串"""
    if random.choice([True, False]):
        return gen_combinational_body(depth-1)
    else:
        return gen_sequential_body(depth-1)

# combinational_body
#     : 'table' combinational_entry+ 'endtable'
#     ;

import random

def gen_combinational_body(depth=3):
    """生成符合 combinational_body 规则的字符串"""
    entries = [gen_combinational_entry(depth-1) for _ in range(random.randint(1, 5))]
    return f"table\n" + "\n".join(entries) + "\nendtable"

# combinational_entry
#     : level_input_list ':' output_symbol ';'
#     ;

def gen_combinational_entry(depth=3):
    """生成符合 combinational_entry 规则的字符串"""
    return f"{gen_level_input_list(depth-1)} : {gen_output_symbol(depth-1)};"


# sequential_body
#     : udp_initial_statement? 'table' sequential_entry+ 'endtable'
#     ;

def gen_sequential_body(depth=3):
    """生成符合 sequential_body 规则的字符串"""
    initial_stmt = f"{gen_udp_initial_statement(depth-1)} " if random.choice([True, False]) else ""
    entries = " ".join(gen_sequential_entry(depth-1) for _ in range(random.randint(1, 5)))
    return f"{initial_stmt}table {entries} endtable"


# udp_initial_statement
#     : 'initial' output_port_identifier '=' init_val ';'
#     ;

def gen_udp_initial_statement(depth=3):
    """生成符合 udp_initial_statement 规则的字符串"""
    return f"initial {gen_output_port_identifier(depth-1)} = {gen_init_val(depth-1)};"


# init_val
#     : binary_number
#     | unsigned_number
#     ;

def gen_init_val(depth=3):
    """生成符合 init_val 规则的字符串"""
    return random.choice([gen_binary_number(depth-1), gen_unsigned_number(depth-1)])

# sequential_entry
#     : seq_input_list ':' current_state ':' next_state ';'
#     ;

def gen_sequential_entry(depth=3):
    """生成符合 sequential_entry 规则的字符串"""
    return f"{gen_seq_input_list(depth-1)} : {gen_current_state(depth-1)} : {gen_next_state(depth-1)};"


# seq_input_list
#     : level_input_list
#     | edge_input_list
#     ;

import random

def gen_seq_input_list(depth=3):
    # 随机选择调用level_input_list或edge_input_list
    if random.choice([True, False]):
        return gen_level_input_list(depth-1)
    else:
        return gen_edge_input_list(depth-1)




# level_input_list
#     : level_symbol+
#     ;

import random

def gen_level_input_list(depth=3):
    # 随机生成1到5个level_symbol，您可以根据需要调整最大数量
    num_symbols = random.randint(1, 5)
    level_symbols = []
    for _ in range(num_symbols):
        level_symbol = gen_level_symbol(depth-1)  # 调用gen_level_symbol函数
        level_symbols.append(level_symbol)
    return level_symbols


# edge_input_list
#     : level_symbol* edge_indicator level_symbol*
#     ;

import random

def gen_edge_input_list(depth=3):
    # 随机生成左侧的level_symbol列表（可能为空）
    left_level_symbols = [gen_level_symbol(depth-1) for _ in range(random.randint(0, 5))]
    
    # 生成edge_indicator
    edge_ind = gen_edge_indicator(depth-1)
    
    # 随机生成右侧的level_symbol列表（可能为空）
    right_level_symbols = [gen_level_symbol(depth-1) for _ in range(random.randint(0, 5))]
    
    # 将所有部分组合成一个列表
    return left_level_symbols + [edge_ind] + right_level_symbols




# edge_indicator
#     : '(' level_symbol level_symbol ')'
#     | edge_symbol
#     ;


import random

def gen_edge_indicator(depth=3):
    # 随机决定使用哪种规则
    if random.choice([True, False]):
        # 使用 '(' level_symbol level_symbol ')'
        left_paren = '('
        level_sym1 = gen_level_symbol(depth-1)
        level_sym2 = gen_level_symbol(depth-1)
        right_paren = ')'
        # 将结果组合成一个列表
        return [left_paren, level_sym1, level_sym2, right_paren]
    else:
        # 使用 edge_symbol
        return gen_edge_symbol(depth-1)


# current_state
#     : level_symbol
#     ;

def gen_current_state(depth=3):
    return gen_level_symbol(depth-1)



# next_state
#     : output_symbol
#     | '-'
#     ;

import random

def gen_next_state(depth=3):
    if random.choice([True, False]):
        # 返回 output_symbol
        return gen_output_symbol(depth-1)
    else:
        # 返回 '-'
        return '-'



# output_symbol
#     : OUTPUT_OR_LEVEL_SYMBOL
#     ;


import random

def gen_output_symbol(depth=3):
    symbols = ['A', 'B', 'C']
    return random.choice(symbols)


# level_symbol
#     : LEVEL_ONLY_SYMBOL
#     | OUTPUT_OR_LEVEL_SYMBOL
#     ;

import random

def gen_level_symbol(depth=3):
    if random.choice([True, False]):
        # 返回 LEVEL_ONLY_SYMBOL
        return gen_LEVEL_ONLY_SYMBOL(depth-1)
    else:
        # 返回 OUTPUT_OR_LEVEL_SYMBOL
        return gen_OUTPUT_OR_LEVEL_SYMBOL(depth-1)




# edge_symbol
#     : EDGE_SYMBOL
#     ;

def gen_edge_symbol(depth=3):
    return gen_EDGE_SYMBOL(depth-1)

# udp_instantiation
#     : udp_identifier drive_strength? delay2? udp_instance (',' udp_instance)* ';'
#     ;

import random

def gen_udp_instantiation(depth=3):
    result = []

    # 生成 udp_identifier
    udp_id = gen_udp_identifier(depth-1)
    result.append(udp_id)

    # 随机决定是否添加 drive_strength
    if random.choice([True, False]):
        drive_strength = gen_drive_strength(depth-1)
        result.append(drive_strength)

    # 随机决定是否添加 delay2
    if random.choice([True, False]):
        delay = gen_delay2(depth-1)
        result.append(delay)

    # 生成第一个 udp_instance
    udp_inst = gen_udp_instance(depth-1)
    result.append(udp_inst)

    # 生成零个或多个 (',' udp_instance)
    while random.choice([True, False]):
        result.append(',')
        udp_inst = gen_udp_instance(depth-1)
        result.append(udp_inst)

    # 添加分号
    result.append(';')

    # 将结果组合成字符串返回
    return ' '.join(result)


# udp_instance
#     : name_of_udp_instance? '(' output_terminal ',' input_terminal (',' input_terminal)* ')'
#     ;

import random

def gen_udp_instance(depth=3):
    result = []

    # 随机决定是否包含 name_of_udp_instance
    if random.choice([True, False]):
        name = gen_name_of_udp_instance(depth-1)
        result.append(name)

    # 添加左括号 '('
    result.append('(')

    # 添加 output_terminal
    output = gen_output_terminal(depth-1)
    result.append(output)

    # 添加逗号 ','
    result.append(',')

    # 添加第一个 input_terminal
    input_terminals = []
    input_terminals.append(gen_input_terminal(depth-1))

    # 随机生成零个或多个 (',' input_terminal)
    while random.choice([True, False]):
        input_terminals.append(',')
        input_terminals.append(gen_input_terminal(depth-1))

    # 将 input_terminals 添加到结果中
    result.extend(input_terminals)

    # 添加右括号 ')'
    result.append(')')

    # 将结果组合成字符串返回
    return ' '.join(result)


# name_of_udp_instance
#     : udp_instance_identifier range_?
#     ;


import random

def gen_name_of_udp_instance(depth=3):
    # 生成 udp_instance_identifier
    udp_id = gen_udp_instance_identifier(depth-1)

    # 随机决定是否添加 range_
    if random.choice([True, False]):
        rng = gen_range_(depth-1)
        return f"{udp_id} {rng}"
    else:
        return udp_id



# continuous_assign
#     : 'assign' drive_strength? delay3? list_of_net_assignments ';'
#     ;

import random

def gen_continuous_assign(depth=3):
    components = []

    # 添加关键字 'assign'
    components.append('assign')

    # 随机决定是否添加 drive_strength
    if random.choice([True, False]):
        components.append(gen_drive_strength(depth-1))

    # 随机决定是否添加 delay3
    if random.choice([True, False]):
        components.append(gen_delay3(depth-1))

    # 添加 list_of_net_assignments
    components.append(gen_list_of_net_assignments(depth-1))

    # 添加分号 ';'
    components.append(';')

    # 将组件组合成字符串并返回
    return ' '.join(components)


 

#  list_of_net_assignments
#     : net_assignment (',' net_assignment)*
#     ;

import random

def gen_list_of_net_assignments(depth=3):
    # 初始化列表，包含第一个 net_assignment
    assignments = [gen_net_assignment(depth-1)]
    
    # 随机添加零个或多个 (',' net_assignment)
    while random.choice([True, False]):
        assignments.append(',')
        assignments.append(gen_net_assignment(depth-1))
    
    # 将列表元素组合成字符串，确保正确的空格和逗号位置
    result = ' '.join(assignments)
    return result

# net_assignment
#     : net_lvalue '=' expression
#     ;

def gen_net_assignment(depth=3):
    # 生成 net_lvalue
    lhs = gen_net_lvalue(depth-1)
    
    # 等号 '='
    equal_sign = '='
    
    # 生成 expression
    expr = gen_expression(depth-1)
    
    # 将各部分组合成字符串
    assignment = f"{lhs} {equal_sign} {expr}"
    
    return assignment



# initial_construct
#     : 'initial' statement
#     ;

def gen_initial_construct(depth=3):
    # 关键字 'initial'
    initial_keyword = 'initial'

    # 生成 statement
    stmt = gen_statement(depth-1)

    # 将结果组合成字符串
    result = f"{initial_keyword} {stmt}"

    return result


# always_construct
#     : 'always' statement
#     ;

def gen_always_construct(depth=3):
    # 关键字 'always'
    always_keyword = 'always'
    
    # 生成 statement
    stmt = gen_statement(depth-1)
    
    # 将结果组合成字符串
    result = f"{always_keyword} {stmt}"
    
    return result




# blocking_assignment
#     : variable_lvalue '=' delay_or_event_control? expression
#     ;


import random

def gen_blocking_assignment(depth=3):
    # Generate the left-hand side variable
    lhs = gen_variable_lvalue(depth-1)
    
    # Assignment operator
    assignment_op = '='
    
    # Decide whether to include delay_or_event_control (optional)
    if random.choice([True, False]):
        delay_event = gen_delay_or_event_control(depth-1)
        # Combine delay_or_event_control with the expression
        rhs = f"{delay_event} {gen_expression(depth-1)}"
    else:
        # Only the expression without delay_or_event_control
        rhs = gen_expression(depth-1)
    
    # Construct the complete blocking assignment
    blocking_assignment = f"{lhs} {assignment_op} {rhs}"
    
    return blocking_assignment



# nonblocking_assignment
#     : variable_lvalue '<=' delay_or_event_control? expression
#     ;

import random

def gen_nonblocking_assignment(depth=3):
    # 生成 variable_lvalue
    lhs = gen_variable_lvalue(depth-1)
    
    # 非阻塞赋值操作符 '<='
    assign_op = '<='
    
    # 随机决定是否包含 delay_or_event_control
    if random.choice([True, False]):
        # 包含 delay_or_event_control
        delay_event = gen_delay_or_event_control(depth-1)
        # 生成 expression
        expr = gen_expression(depth-1)
        # 将 delay_or_event_control 与 expression 合并
        rhs = f"{delay_event} {expr}"
    else:
        # 不包含 delay_or_event_control，直接生成 expression
        rhs = gen_expression(depth-1)
    
    # 将所有部分组合成字符串
    nonblocking_assignment = f"{lhs} {assign_op} {rhs}"
    
    return nonblocking_assignment

# procedural_continuous_assignments
#     : 'assign' variable_assignment
#     | 'deassign' variable_lvalue
#     | 'force' variable_assignment
#     | 'release' variable_lvalue
#     ;

import random

def gen_procedural_continuous_assignments(depth=3):
    options = ['assign', 'deassign', 'force', 'release']
    choice = random.choice(options)

    if choice == 'assign':
        # 'assign' variable_assignment
        return f"{choice} {gen_variable_assignment(depth-1)}"
    elif choice == 'deassign':
        # 'deassign' variable_lvalue
        return f"{choice} {gen_variable_lvalue(depth-1)}"
    elif choice == 'force':
        # 'force' variable_assignment
        return f"{choice} {gen_variable_assignment(depth-1)}"
    elif choice == 'release':
        # 'release' variable_lvalue
        return f"{choice} {gen_variable_lvalue(depth-1)}"



# variable_assignment
#     : variable_lvalue '=' expression
#     ;


def gen_variable_assignment(depth=3):
    # 生成 variable_lvalue
    lhs = gen_variable_lvalue(depth-1)
    
    # 等号 '='
    assignment_operator = '='
    
    # 生成 expression
    rhs = gen_expression(depth-1)
    
    # 将各部分组合成完整的赋值语句
    variable_assignment = f"{lhs} {assignment_operator} {rhs}"
    
    return variable_assignment



# par_block
#     : 'fork' (block_name block_item_declaration*)? statement* 'join'
#     ;

import random

def gen_par_block(depth=3):
    components = []

    # 添加关键字 'fork'
    components.append('fork')

    # 随机决定是否包含可选部分 (block_name block_item_declaration*)
    if random.choice([True, False]):
        # 添加 block_name
        block_name = gen_block_name(depth-1)
        components.append(block_name)
        
        # 添加零个或多个 block_item_declaration
        while random.choice([True, False]):
            block_item_decl = gen_block_item_declaration(depth-1)
            components.append(block_item_decl)
    
    # 添加零个或多个 statement
    while random.choice([True, False]):
        stmt = gen_statement(depth-1)
        components.append(stmt)
    
    # 添加关键字 'join'
    components.append('join')
    
    # 将组件组合成字符串，组件之间用换行符分隔，以提高可读性
    result = '\n'.join(components)
    return result


# block_name
#     : ':' block_identifier
#     ;

def gen_block_name(depth=3):
    # 返回 ':' 加上 block_identifier
    return ': ' + gen_block_identifier(depth-1)




# seq_block
#     : 'begin' (block_name block_item_declaration*)? statement* 'end'
#     ;


import random

def gen_seq_block(depth=3):
    components = []

    # 添加关键字 'begin'
    components.append('begin')

    # 随机决定是否包含可选部分 (block_name block_item_declaration*)
    if random.choice([True, False]):
        # 添加 block_name
        block_name = gen_block_name(depth-1)
        components.append(block_name)

        # 添加零个或多个 block_item_declaration
        while random.choice([True, False]):
            block_item_decl = gen_block_item_declaration(depth-1)
            components.append(block_item_decl)

    # 添加零个或多个 statement
    while random.choice([True, False]):
        stmt = gen_statement(depth-1)
        components.append(stmt)

    # 添加关键字 'end'
    components.append('end')

    # 将组件组合成字符串，组件之间用换行符分隔，以提高可读性
    result = '\n'.join(components)
    return result


# statement
#     : attribute_instance* blocking_assignment ';'
#     | attribute_instance* case_statement
#     | attribute_instance* conditional_statement
#     | attribute_instance* disable_statement
#     | attribute_instance* event_trigger
#     | attribute_instance* loop_statement
#     | attribute_instance* nonblocking_assignment ';'
#     | attribute_instance* par_block
#     | attribute_instance* procedural_continuous_assignments ';'
#     | attribute_instance* procedural_timing_control_statement
#     | attribute_instance* seq_block
#     | attribute_instance* system_task_enable
#     | attribute_instance* task_enable
#     | attribute_instance* wait_statement
#     ;


import random

def gen_statement(depth=3):
    components = []
    
    # 随机生成零个或多个 attribute_instance
    while random.choice([True, False]):
        attr_instance = gen_attribute_instance(depth-1)
        components.append(attr_instance)
    
    # 定义可能的语句类型及其是否需要分号
    statement_types = [
        ('blocking_assignment', True),
        ('case_statement', False),
        ('conditional_statement', False),
        ('disable_statement', False),
        ('event_trigger', False),
        ('loop_statement', False),
        ('nonblocking_assignment', True),
        ('par_block', False),
        ('procedural_continuous_assignments', True),
        ('procedural_timing_control_statement', False),
        ('seq_block', False),
        ('system_task_enable', False),
        ('task_enable', False),
        ('wait_statement', False)
    ]
    
    # 随机选择一种语句类型
    stmt_type, needs_semicolon = random.choice(statement_types)
    
    # 调用相应的生成函数
    stmt_generator = globals().get(f"gen_{stmt_type}")
    if stmt_generator:
        stmt = stmt_generator(depth-1)
        components.append(stmt)
    else:
        # 如果生成函数不存在，使用占位符
        components.append(f"<{stmt_type}>")
    
    # 如果需要分号，添加分号
    if needs_semicolon:
        components.append(';')
    
    # 将组件组合成字符串，并返回
    result = ' '.join(components)
    return result


# statement_or_null
#     : statement
#     | attribute_instance* ';'
#     ;


import random

def gen_statement_or_null(depth=3):
    components = []
    
    # 随机选择生成 'statement' 或 'attribute_instance* ;'
    if random.choice([True, False]):
        # 生成一个完整的 statement
        stmt = gen_statement(depth-1)
        components.append(stmt)
    else:
        # 生成零个或多个 attribute_instance
        while random.choice([True, False]):
            attr_instance = gen_attribute_instance(depth-1)
            components.append(attr_instance)
        # 添加分号 ';'
        components.append(';')
    
    # 将组件组合成字符串，使用空格分隔
    result = ' '.join(components)
    return result



# function_statement
#     : statement
#     ;

def gen_function_statement(depth=3):
    return gen_statement(depth-1)



# delay_control
#     : '#' delay_value
#     | '#' '(' mintypmax_expression ')'
#     ;

import random

def gen_delay_control(depth=3):
    if random.choice([True, False]):
        # '#' delay_value
        return '#' + gen_delay_value(depth-1)
    else:
        # '#' '(' mintypmax_expression ')'
        return '#' + '(' + gen_mintypmax_expression(depth-1) + ')'


# delay_or_event_control
#     : delay_control
#     | event_control
#     | 'repeat' '(' expression ')' event_control
#     ;

import random

def gen_delay_or_event_control(depth=3):
    # 随机选择一种形式
    options = ['delay_control', 'event_control', 'repeat']
    choice = random.choice(options)
    
    if choice == 'delay_control':
        # 调用 gen_delay_control(depth-1)
        return gen_delay_control(depth-1)
    elif choice == 'event_control':
        # 调用 gen_event_control(depth-1)
        return gen_event_control(depth-1)
    else:
        # 生成 'repeat ( expression ) event_control'
        repeat_keyword = 'repeat'
        left_paren = '('
        expr = gen_expression(depth-1)
        right_paren = ')'
        event_ctrl = gen_event_control(depth-1)
        
        # 组合成字符串
        return f"{repeat_keyword} {left_paren}{expr}{right_paren} {event_ctrl}"



# disable_statement
#     : 'disable' hierarchical_identifier ';'
#     ;


def gen_disable_statement(depth=3):
    # 关键字 'disable'
    disable_keyword = 'disable'
    
    # 调用 gen_hierarchical_identifier(depth-1) 生成 hierarchical_identifier
    hier_id = gen_hierarchical_identifier(depth-1)
    
    # 分号 ';'
    semicolon = ';'
    
    # 将各部分组合成字符串
    disable_stmt = f"{disable_keyword} {hier_id} {semicolon}"
    
    return disable_stmt




# event_control
#     : '@' hierarchical_identifier
#     | '@' '(' event_expression ')'
#     | '@' '*'
#     | '@' '(' '*' ')'
#     ;


import random

def gen_event_control(depth=3):
    # 定义可能的形式
    options = ['hierarchical_identifier', 'event_expression', 'star', 'star_in_parens']
    choice = random.choice(options)

    if choice == 'hierarchical_identifier':
        # '@' hierarchical_identifier
        return '@' + gen_hierarchical_identifier(depth-1)
    elif choice == 'event_expression':
        # '@' '(' event_expression ')'
        return '@(' + gen_event_expression(depth-1) + ')'
    elif choice == 'star':
        # '@' '*'
        return '@' + '*'
    elif choice == 'star_in_parens':
        # '@' '(' '*' ')'
        return '@(' + '*' + ')'




# event_trigger
#     : '->' hierarchical_identifier bit_select? ';'
#     ;


import random

def gen_event_trigger(depth=3):
    # 箭头符号 '->'
    arrow = '->'

    # 生成 hierarchical_identifier
    hier_id = gen_hierarchical_identifier(depth-1)

    # 随机决定是否包含可选的 bit_select
    if random.choice([True, False]):
        bit_sel = gen_bit_select(depth-1)
        hier_id_with_bit_select = f"{hier_id}{bit_sel}"
    else:
        hier_id_with_bit_select = hier_id

    # 分号 ';'
    semicolon = ';'

    # 将所有部分组合成字符串
    event_trigger = f"{arrow} {hier_id_with_bit_select} {semicolon}"

    return event_trigger



# event_expression
#     : expression
#     | 'posedge' expression
#     | 'negedge' expression
#     | event_expression 'or' event_expression
#     | event_expression ',' event_expression
#     ;

import random

def gen_event_expression(depth=3):
    if depth <= 0:
        # 当递归深度达到 0 时，返回最简单的 expression
        return gen_simple_event_expression(depth-1)

    # 定义可能的形式
    options = [
        'expression',
        'posedge',
        'negedge',
        'or',
        'comma'
    ]
    choice = random.choice(options)

    if choice == 'expression':
        # 返回 expression
        return gen_expression(depth-1)
    elif choice == 'posedge':
        # 返回 'posedge' expression
        expr = gen_expression(depth-1)
        return f"posedge {expr}"
    elif choice == 'negedge':
        # 返回 'negedge' expression
        expr = gen_expression(depth-1)
        return f"negedge {expr}"
    elif choice == 'or':
        # 返回 event_expression 'or' event_expression
        left = gen_event_expression(depth - 1)
        right = gen_event_expression(depth - 1)
        return f"{left} or {right}"
    elif choice == 'comma':
        # 返回 event_expression ',' event_expression
        left = gen_event_expression(depth - 1)
        right = gen_event_expression(depth - 1)
        return f"{left}, {right}"

def gen_simple_event_expression(depth=3):
    # 仅生成最简单的 expression，避免进一步递归
    return gen_expression(depth-1)



# procedural_timing_control
#     : delay_control
#     | event_control
#     ;

import random

def gen_procedural_timing_control(depth=3):
    # 随机选择 'delay_control' 或 'event_control'
    if random.choice([True, False]):
        # 调用 gen_delay_control(depth-1)
        return gen_delay_control(depth-1)
    else:
        # 调用 gen_event_control(depth-1)
        return gen_event_control(depth-1)

# procedural_timing_control_statement
#     : procedural_timing_control statement_or_null
#     ;

def gen_procedural_timing_control_statement(depth=3):
    # 调用 gen_procedural_timing_control(depth-1) 生成 procedural_timing_control
    timing_control = gen_procedural_timing_control(depth-1)
    
    # 调用 gen_statement_or_null(depth-1) 生成 statement_or_null
    stmt_or_null = gen_statement_or_null(depth-1)
    
    # 将两部分组合成字符串
    return f"{timing_control} {stmt_or_null}"

# wait_statement
#     : 'wait' '(' expression ')' statement_or_null
#     ;

def gen_wait_statement(depth=3):
    # 关键字 'wait'
    wait_keyword = 'wait'
    
    # 左括号 '('
    left_paren = '('
    
    # 调用 gen_expression(depth-1) 生成 expression
    expr = gen_expression(depth-1)
    
    # 右括号 ')'
    right_paren = ')'
    
    # 调用 gen_statement_or_null(depth-1) 生成 statement_or_null
    stmt_or_null = gen_statement_or_null(depth-1)
    
    # 将各部分组合成字符串
    wait_stmt = f"{wait_keyword} {left_paren}{expr}{right_paren} {stmt_or_null}"
    
    return wait_stmt



# conditional_statement
#     : 'if' '(' expression ')' statement_or_null ('else' statement_or_null)?
#     ;

import random

def gen_conditional_statement(depth=3):
    # 关键字 'if'
    if_keyword = 'if'

    # 左括号 '('
    left_paren = '('

    # 生成 expression
    condition = gen_expression(depth-1)

    # 右括号 ')'
    right_paren = ')'

    # 生成 statement_or_null
    then_stmt = gen_statement_or_null(depth-1)

    # 随机决定是否包含可选的 'else' 分支
    if random.choice([True, False]):
        # 包含 'else' 分支
        else_keyword = 'else'
        else_stmt = gen_statement_or_null(depth-1)

        # 组合成完整的 if-else 结构
        conditional_stmt = f"{if_keyword} {left_paren}{condition}{right_paren} {then_stmt}\n{else_keyword} {else_stmt}"
    else:
        # 不包含 'else' 分支
        # 组合成只有 if 的结构
        conditional_stmt = f"{if_keyword} {left_paren}{condition}{right_paren} {then_stmt}"

    return conditional_stmt




# case_statement
#     : 'case' '(' expression ')' case_item+ 'endcase'
#     | 'casez' '(' expression ')' case_item+ 'endcase'
#     | 'casex' '(' expression ')' case_item+ 'endcase'
#     ;

import random

def gen_case_statement(depth=3):
    # 随机选择 'case'、'casez' 或 'casex'
    case_types = ['case', 'casez', 'casex']
    case_keyword = random.choice(case_types)

    # 左括号 '(' 和右括号 ')'
    left_paren = '('
    right_paren = ')'

    # 生成 expression
    expr = gen_expression(depth-1)

    # 生成一个或多个 case_item
    num_case_items = random.randint(1, 5)  # 您可以根据需要调整数量范围
    case_items = []
    for _ in range(num_case_items):
        case_item = gen_case_item(depth-1)
        case_items.append(case_item)

    # 开始构建 case_statement 字符串
    case_statement_str = f"{case_keyword} {left_paren}{expr}{right_paren}\n"

    # 添加 case_items
    for item in case_items:
        case_statement_str += f"    {item}\n"  # 缩进以提高可读性

    # 添加 'endcase'
    case_statement_str += "endcase"

    return case_statement_str


# case_item
#     : expression (',' expression)* ':' statement_or_null
#     | 'default' ':'? statement_or_null
#     ;


import random

def gen_case_item(depth=3):
    components = []

    # 随机决定生成哪种形式：表达式形式或 'default' 形式
    if random.choice([True, False]):
        # 生成表达式形式
        # 随机生成 1 到 3 个 expression
        num_expressions = random.randint(1, 3)
        expressions = [gen_expression(depth-1) for _ in range(num_expressions)]
        expression_str = ', '.join(expressions)
        components.append(expression_str)

        # 添加冒号 ':'
        components.append(':')

        # 生成 statement_or_null
        stmt = gen_statement_or_null(depth-1)
        components.append(stmt)
    else:
        # 生成 'default' 形式
        components.append('default')

        # 可选地添加冒号 ':'
        if random.choice([True, False]):
            components.append(':')
        
        # 生成 statement_or_null
        stmt = gen_statement_or_null(depth-1)
        components.append(stmt)

    # 将组件组合成字符串
    case_item_str = ' '.join(components)
    return case_item_str




# loop_statement
#     : 'forever' statement
#     | 'repeat' '(' expression ')' statement
#     | 'while' '(' expression ')' statement
#     | 'for' '(' variable_assignment ';' expression ';' variable_assignment ')' statement
#     ;

import random

def gen_loop_statement(depth=3):
    options = ['forever', 'repeat', 'while', 'for']
    choice = random.choice(options)

    if choice == 'forever':
        # 'forever' statement
        stmt = gen_statement(depth-1)
        return f"forever {stmt}"

    elif choice == 'repeat':
        # 'repeat' '(' expression ')' statement
        expr = gen_expression(depth-1)
        stmt = gen_statement(depth-1)
        return f"repeat ({expr}) {stmt}"

    elif choice == 'while':
        # 'while' '(' expression ')' statement
        expr = gen_expression(depth-1)
        stmt = gen_statement(depth-1)
        return f"while ({expr}) {stmt}"

    elif choice == 'for':
        # 'for' '(' variable_assignment ';' expression ';' variable_assignment ')' statement
        init_assignment = gen_variable_assignment(depth-1)
        condition = gen_expression(depth-1)
        incr_assignment = gen_variable_assignment(depth-1)
        stmt = gen_statement(depth-1)
        return f"for ({init_assignment}; {condition}; {incr_assignment}) {stmt}"



# system_task_enable
#     : system_task_identifier sys_task_en_port_list? ';'
#     ;

import random

def gen_system_task_enable(depth=3):
    # 生成 system_task_identifier
    task_id = gen_system_task_identifier(depth-1)
    
    # 随机决定是否包含可选的 sys_task_en_port_list
    if random.choice([True, False]):
        port_list = gen_sys_task_en_port_list(depth-1)
        task_with_port_list = f"{task_id} {port_list}"
    else:
        task_with_port_list = task_id
    
    # 分号 ';'
    semicolon = ';'
    
    # 将所有部分组合成字符串
    system_task_enable = f"{task_with_port_list} {semicolon}"
    
    return system_task_enable




# sys_task_en_port_list
#     : '(' sys_task_en_port_item (',' sys_task_en_port_item)* ')'
#     ;

import random

def gen_sys_task_en_port_list(depth=3):
    # 左括号 '('
    left_paren = '('

    # 生成第一个 sys_task_en_port_item
    first_port_item = gen_sys_task_en_port_item(depth-1)

    # 随机生成零个或多个 sys_task_en_port_item，最多生成 5 个
    num_additional_items = random.randint(0, 5)
    additional_items = [gen_sys_task_en_port_item(depth-1) for _ in range(num_additional_items)]

    # 用逗号和空格连接所有端口项
    all_port_items = ', '.join([first_port_item] + additional_items)

    # 右括号 ')'
    right_paren = ')'

    # 将所有部分组合成字符串
    sys_task_en_port_list = f"{left_paren}{all_port_items}{right_paren}"

    return sys_task_en_port_list

# sys_task_en_port_item
#     : expression?
#     ;

import random

def gen_sys_task_en_port_item(depth=3):
    """
    生成符合 sys_task_en_port_item 产生式的字符串：
         sys_task_en_port_item : expression?
    
    说明：
      - expression 是可选项，所以随机决定生成 expression 部分；
      - 如果不生成，则返回空字符或其他默认值。
    """
    # 用随机选择决定是否生成 expression 部分
    if random.choice([True, False]):
        return gen_expression(depth-1)
    else:
        return ""  # 不生成任何 expression，返回空字符串





# task_enable
#     : hierarchical_identifier task_en_port_list? ';'
#     ;

import random

def gen_task_enable(depth=3):
    # 生成 hierarchical_identifier 部分
    hier_id = gen_hierarchical_identifier(depth-1)
    
    # 随机决定是否包含可选的 task_en_port_list
    if random.choice([True, False]):
        port_list = gen_task_en_port_list(depth-1)
        task_enable_str = f"{hier_id} {port_list} ;"
    else:
        task_enable_str = f"{hier_id} ;"
    
    return task_enable_str

# 以下为占位函数，需在其他地方实现具体生成逻辑




# task_en_port_list
#     : '(' expression (',' expression)* ')'
#     ;

import random

def gen_task_en_port_list(depth=3):
    # 左括号
    left_paren = '('
    # 生成第一个必须的 expression
    first_expr = gen_expression(depth-1)
    
    # 随机生成 0 到 3 个额外的 expression 项
    num_extra = random.randint(0, 3)
    extra_exprs = [gen_expression(depth-1) for _ in range(num_extra)]
    
    # 使用逗号连接所有 expression
    exprs = [first_expr] + extra_exprs
    expr_string = ', '.join(exprs)
    
    # 右括号
    right_paren = ')'
    
    # 组合并返回完整的 task_en_port_list 字符串
    return f"{left_paren}{expr_string}{right_paren}"



# specify_block
#     : 'specify' specify_item* 'endspecify'
#     ;


import random

def gen_specify_block(depth=3):
    # 初始化结果列表，首先添加关键字 'specify'
    components = []
    components.append("specify")
    
    # 随机生成 0 到 5 个 specify_item
    num_items = random.randint(0, 5)
    for _ in range(num_items):
        components.append(gen_specify_item(depth-1))
    
    # 添加结束关键字 'endspecify'
    components.append("endspecify")
    
    # 将各部分组合成字符串，使用换行符分隔
    return "\n".join(components)

# specify_item
#     : specparam_declaration
#     | pulsestyle_declaration
#     | showcancelled_declaration
#     | path_declaration
#     | system_timing_check
#     ;

import random

def gen_specify_item(depth=3):
    # 定义可能的选项对应的生成函数名称
    options = [
        'specparam_declaration',
        'pulsestyle_declaration',
        'showcancelled_declaration',
        'path_declaration',
        'system_timing_check'
    ]
    # 随机选择一种替代形式
    choice = random.choice(options)
    
    if choice == 'specparam_declaration':
        return gen_specparam_declaration(depth-1)
    elif choice == 'pulsestyle_declaration':
        return gen_pulsestyle_declaration(depth-1)
    elif choice == 'showcancelled_declaration':
        return gen_showcancelled_declaration(depth-1)
    elif choice == 'path_declaration':
        return gen_path_declaration(depth-1)
    elif choice == 'system_timing_check':
        return gen_system_timing_check(depth-1)



# pulsestyle_declaration
#     : 'pulsestyle_onevent' list_of_path_outputs ';'
#     | 'pulsestyle_ondetect' list_of_path_outputs ';'
#     ;

import random

def gen_pulsestyle_declaration(depth=3):
    # 随机选择生成 'pulsestyle_onevent' 或 'pulsestyle_ondetect' 的替代方案
    if random.choice([True, False]):
        # 'pulsestyle_onevent' list_of_path_outputs ';'
        keyword = "pulsestyle_onevent"
    else:
        # 'pulsestyle_ondetect' list_of_path_outputs ';'
        keyword = "pulsestyle_ondetect"
    
    # 调用对应的生成函数来生成 list_of_path_outputs
    list_outputs = gen_list_of_path_outputs(depth-1)
    
    # 分号
    semicolon = ';'
    
    # 组合各个部分，返回生成的结果字符串
    return f"{keyword} {list_outputs} {semicolon}"




# showcancelled_declaration
#     : 'showcancelled' list_of_path_outputs ';'
#     | 'noshowcancelled' list_of_path_outputs ';'
#     ;

import random

def gen_showcancelled_declaration(depth=3):
    # 随机选择 'showcancelled' 或 'noshowcancelled'
    if random.choice([True, False]):
        keyword = "showcancelled"
    else:
        keyword = "noshowcancelled"
    
    # 调用生成 list_of_path_outputs 的函数（该函数的具体实现由其他地方提供）
    list_outputs = gen_list_of_path_outputs(depth-1)
    
    # 返回组合后的完整字符串，注意末尾添加分号
    return f"{keyword} {list_outputs} ;"




# path_declaration
#     : simple_path_declaration ';'
#     | edge_sensitive_path_declaration ';'
#     | state_dependent_path_declaration ';'
#     ;

import random

def gen_path_declaration(depth=3):
    # 定义可能的替代形式
    options = [
        'simple_path_declaration',
        'edge_sensitive_path_declaration',
        'state_dependent_path_declaration'
    ]
    choice = random.choice(options)
    
    if choice == 'simple_path_declaration':
        decl = gen_simple_path_declaration(depth-1)
    elif choice == 'edge_sensitive_path_declaration':
        decl = gen_edge_sensitive_path_declaration(depth-1)
    else:
        decl = gen_state_dependent_path_declaration(depth-1)
    
    # 添加分号 ';' 结束路径声明
    return f"{decl} ;"


# simple_path_declaration
#     : parallel_path_description '=' path_delay_value
#     | full_path_description '=' path_delay_value
#     ;

import random

def gen_simple_path_declaration(depth=3):
    # 随机选择生成 parallel_path_description 还是 full_path_description 的形式
    if random.choice([True, False]):
        path_desc = gen_parallel_path_description(depth-1)
    else:
        path_desc = gen_full_path_description(depth-1)
    
    # 生成 path_delay_value
    delay_value = gen_path_delay_value(depth-1)
    
    # 组合表示 simple_path_declaration 的字符串
    return f"{path_desc} = {delay_value}"




# parallel_path_description
#     : '(' specify_input_terminal_descriptor polarity_operator? '=>' specify_output_terminal_descriptor ')'
#     ;


import random

def gen_parallel_path_description(depth=3):
    # 生成左括号 '('
    open_paren = '('
    
    # 生成 specify_input_terminal_descriptor 部分
    input_desc = gen_specify_input_terminal_descriptor(depth-1)
    
    # 随机决定是否生成可选的 polarity_operator 部分
    if random.choice([True, False]):
        polarity = gen_polarity_operator(depth-1)
        # 在 polarity_operator 前添加一个空格以分隔
        polarity_str = f" {polarity}"
    else:
        polarity_str = ""
    
    # 固定符号 '=>'
    arrow = " => "
    
    # 生成 specify_output_terminal_descriptor 部分
    output_desc = gen_specify_output_terminal_descriptor(depth-1)
    
    # 生成右括号 ')'
    close_paren = ')'
    
    # 组合所有部分，形成完整的 parallel_path_description
    return f"{open_paren}{input_desc}{polarity_str}{arrow}{output_desc}{close_paren}"


# full_path_description
#     : '(' list_of_path_inputs polarity_operator? '*>' list_of_path_outputs ')'
#     ;


import random

def gen_full_path_description(depth=3):
    # 左括号
    left_paren = '('
    
    # 生成 list_of_path_inputs
    inputs = gen_list_of_path_inputs(depth-1)
    
    # 随机决定是否生成可选的 polarity_operator
    if random.choice([True, False]):
        pol_op = gen_polarity_operator(depth-1)
        # 在 polarity_operator 前添加一个空格以便区分
        pol_op_str = f" {pol_op}"
    else:
        pol_op_str = ""
    
    # 固定符号 '*>'
    arrow = " *>"
    
    # 生成 list_of_path_outputs
    outputs = gen_list_of_path_outputs(depth-1)
    
    # 右括号
    right_paren = ')'
    
    # 组合所有部分
    return f"{left_paren}{inputs}{pol_op_str}{arrow}{outputs}{right_paren}"



# list_of_path_inputs
#     : specify_input_terminal_descriptor (',' specify_input_terminal_descriptor)*
#     ;


import random

def gen_list_of_path_inputs(depth=3):
    # 生成第一个必有的 specify_input_terminal_descriptor
    first_input = gen_specify_input_terminal_descriptor(depth-1)
    
    # 随机生成 0 到 3 个额外的 specify_input_terminal_descriptor
    num_additional = random.randint(0, 3)
    additional_inputs = [gen_specify_input_terminal_descriptor(depth-1) for _ in range(num_additional)]
    
    # 将所有输入项用逗号和空格连接起来
    all_inputs = [first_input] + additional_inputs
    return ', '.join(all_inputs)



# list_of_path_outputs
#     : specify_output_terminal_descriptor (',' specify_output_terminal_descriptor)*
#     ;


import random

def gen_list_of_path_outputs(depth=3):
    # 生成第一个必有的 specify_output_terminal_descriptor
    first_output = gen_specify_output_terminal_descriptor(depth-1)
    
    # 随机生成 0 到 3 个额外的 specify_output_terminal_descriptor
    num_additional = random.randint(0, 3)
    additional_outputs = [gen_specify_output_terminal_descriptor(depth-1) for _ in range(num_additional)]
    
    # 将所有输出项用逗号和空格连接起来
    outputs = [first_output] + additional_outputs
    return ', '.join(outputs)




# specify_input_terminal_descriptor
#     : input_identifier ('[' constant_range_expression ']')?
#     ;


def gen_specify_input_terminal_descriptor(depth=3):
    """生成符合 specify_input_terminal_descriptor 规则的字符串"""
    if random.choice([True, False]):
        return f"{gen_input_identifier(depth-1)}[{gen_constant_range_expression(depth-1)}]"
    return gen_input_identifier(depth-1)

# specify_output_terminal_descriptor
#     : output_identifier ('[' constant_range_expression ']')?
#     ;


def gen_specify_output_terminal_descriptor(depth=3):
    """生成符合 specify_output_terminal_descriptor 规则的字符串"""
    if random.choice([True, False]):
        return f"{gen_output_identifier(depth-1)}[{gen_constant_range_expression(depth-1)}]"
    return gen_output_identifier(depth-1)


# input_identifier
#     : port_identifier
#     ;


def gen_input_identifier(depth=3):
    return gen_port_identifier(depth-1)

# output_identifier
#     : port_identifier
#     ;

def gen_output_identifier(depth=3):
    return gen_port_identifier(depth-1)

# path_delay_value
#     : list_of_path_delay_expressions
#     | '(' list_of_path_delay_expressions ')'
#     ;


import random

def gen_path_delay_value(depth=3):
    """生成符合 path_delay_value 规则的字符串"""
    if random.choice([True, False]):
        return gen_list_of_path_delay_expressions(depth-1)
    else:
        return f"({gen_list_of_path_delay_expressions(depth-1)})"

# list_of_path_delay_expressions
#     : t_path_delay_expression
#     | trise_path_delay_expression ',' tfall_path_delay_expression (',' tz_path_delay_expression)?
#     | t01_path_delay_expression ',' t10_path_delay_expression ',' t0z_path_delay_expression ',' tz1_path_delay_expression ','
#         t1z_path_delay_expression ',' tz0_path_delay_expression (
#         ',' t0x_path_delay_expression ',' tx1_path_delay_expression ',' t1x_path_delay_expression ',' tx0_path_delay_expression ','
#             txz_path_delay_expression ',' tzx_path_delay_expression
#     )?
#     ;

import random

def gen_list_of_path_delay_expressions(depth=3):
    """生成符合 list_of_path_delay_expressions 规则的字符串"""
    branch = random.choice([1, 2, 3])
    
    if branch == 1:
        # 分支1: 单个 t_path_delay_expression
        return gen_t_path_delay_expression(depth-1)
    
    elif branch == 2:
        # 分支2: trise_path_delay_expression, tfall_path_delay_expression, 可选 tz_path_delay_expression
        result = f"{gen_trise_path_delay_expression(depth-1)}, {gen_tfall_path_delay_expression(depth-1)}"
        if random.choice([True, False]):
            result += f", {gen_tz_path_delay_expression(depth-1)}"
        return result
    
    else:
        # 分支3: 必须有 6 个表达式，然后可选附加 6 个表达式
        mandatory_exprs = [
            gen_t01_path_delay_expression(depth-1),
            gen_t10_path_delay_expression(depth-1),
            gen_t0z_path_delay_expression(depth-1),
            gen_tz1_path_delay_expression(depth-1),
            gen_t1z_path_delay_expression(depth-1),
            gen_tz0_path_delay_expression(depth-1)
        ]
        result = ", ".join(mandatory_exprs)
        if random.choice([True, False]):
            extra_exprs = [
                gen_t0x_path_delay_expression(depth-1),
                gen_tx1_path_delay_expression(depth-1),
                gen_t1x_path_delay_expression(depth-1),
                gen_tx0_path_delay_expression(depth-1),
                gen_txz_path_delay_expression(depth-1),
                gen_tzx_path_delay_expression(depth-1)
            ]
            result += ", " + ", ".join(extra_exprs)
        return result


# t_path_delay_expression
#     : path_delay_expression
#     ;

# trise_path_delay_expression
#     : path_delay_expression
#     ;

# tfall_path_delay_expression
#     : path_delay_expression
#     ;

# tz_path_delay_expression
#     : path_delay_expression
#     ;

# t01_path_delay_expression
#     : path_delay_expression
#     ;

# t10_path_delay_expression
#     : path_delay_expression
#     ;

# t0z_path_delay_expression
#     : path_delay_expression
#     ;

# tz1_path_delay_expression
#     : path_delay_expression
#     ;

# t1z_path_delay_expression
#     : path_delay_expression
#     ;

# tz0_path_delay_expression
#     : path_delay_expression
#     ;

# t0x_path_delay_expression
#     : path_delay_expression
#     ;

# tx1_path_delay_expression
#     : path_delay_expression
#     ;

# t1x_path_delay_expression
#     : path_delay_expression
#     ;

# tx0_path_delay_expression
#     : path_delay_expression
#     ;

# txz_path_delay_expression
#     : path_delay_expression
#     ;

# tzx_path_delay_expression
#     : path_delay_expression
#     ;


def gen_t_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_trise_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tfall_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tz_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_t01_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_t10_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_t0z_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tz1_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_t1z_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tz0_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_t0x_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tx1_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_t1x_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tx0_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_txz_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

def gen_tzx_path_delay_expression(depth=3):
    return gen_path_delay_expression(depth-1)

# path_delay_expression
#     : constant_mintypmax_expression
#     ;


def gen_path_delay_expression(depth=3):
    return gen_constant_mintypmax_expression(depth-1)



# edge_sensitive_path_declaration
#     : parallel_edge_sensitive_path_description '=' path_delay_value
#     | full_edge_sensitive_path_description '=' path_delay_value
#     ;

# parallel_edge_sensitive_path_description
#     : '(' edge_identifier? specify_input_terminal_descriptor '=>' '(' specify_output_terminal_descriptor polarity_operator? ':' data_source_expression
#         ')' ')'
#     ;

# full_edge_sensitive_path_description
#     : '(' edge_identifier? list_of_path_inputs '*>' '(' list_of_path_outputs polarity_operator? ':' data_source_expression ')' ')'
#     ;

import random

def gen_edge_sensitive_path_declaration(depth=3):
    """生成符合 edge_sensitive_path_declaration 规则的字符串"""
    # 随机选择并生成 parallel 或 full edge sensitive path description
    if random.choice([True, False]):
        description = gen_parallel_edge_sensitive_path_description(depth-1)
    else:
        description = gen_full_edge_sensitive_path_description(depth-1)
    delay = gen_path_delay_value(depth-1)
    return f"{description} = {delay}"

def gen_parallel_edge_sensitive_path_description(depth=3):
    """生成符合 parallel_edge_sensitive_path_description 规则的字符串"""
    result = "("
    # 可选生成 edge_identifier
    if random.choice([True, False]):
        result += gen_edge_identifier(depth-1) + " "
    # 生成 specify_input_terminal_descriptor
    result += f"{gen_specify_input_terminal_descriptor(depth-1)} => ("
    # 生成 specify_output_terminal_descriptor
    result += gen_specify_output_terminal_descriptor(depth-1)
    # 可选生成 polarity_operator
    if random.choice([True, False]):
        result += f" {gen_polarity_operator(depth-1)}"
    # 生成 data_source_expression
    result += f": {gen_data_source_expression(depth-1)})"
    result += ")"
    return result

def gen_full_edge_sensitive_path_description(depth=3):
    """生成符合 full_edge_sensitive_path_description 规则的字符串"""
    result = "("
    # 可选生成 edge_identifier
    if random.choice([True, False]):
        result += gen_edge_identifier(depth-1) + " "
    # 生成 list_of_path_inputs
    result += f"{gen_list_of_path_inputs(depth-1)} *>("
    # 生成 list_of_path_outputs
    result += gen_list_of_path_outputs(depth-1)
    # 可选生成 polarity_operator
    if random.choice([True, False]):
        result += f" {gen_polarity_operator(depth-1)}"
    # 生成 data_source_expression
    result += f": {gen_data_source_expression(depth-1)})"
    result += ")"
    return result


# data_source_expression
#     : expression
#     ;

# edge_identifier
#     : 'posedge'
#     | 'negedge'
#     ;

# state_dependent_path_declaration
#     : 'if' '(' module_path_expression ')' simple_path_declaration
#     | 'if' '(' module_path_expression ')' edge_sensitive_path_declaration
#     | 'ifnone' simple_path_declaration
#     ;

# polarity_operator
#     : '+'
#     | '-'
#     ;

import random

def gen_data_source_expression(depth=3):
    """生成符合 ata_source_expression 规则的字符串"""
    return gen_expression(depth-1)

def gen_edge_identifier(depth=3):
    """生成符合 edge_identifier 规则的字符串"""
    return random.choice(["posedge", "negedge"])

def gen_state_dependent_path_declaration(depth=3):
    """生成符合 state_dependent_path_declaration 规则的字符串"""
    branch = random.choice([1, 2, 3])
    if branch == 1:
        # 'if' '(' module_path_expression ')' simple_path_declaration
        return f"if ({gen_module_path_expression(depth-1)}) {gen_simple_path_declaration(depth-1)}"
    elif branch == 2:
        # 'if' '(' module_path_expression ')' edge_sensitive_path_declaration
        return f"if ({gen_module_path_expression(depth-1)}) {gen_edge_sensitive_path_declaration(depth-1)}"
    else:
        # 'ifnone' simple_path_declaration
        return f"ifnone {gen_simple_path_declaration(depth-1)}"

def gen_polarity_operator(depth=3):
    """生成符合 polarity_operator 规则的字符串"""
    return random.choice(["+", "-"])

# system_timing_check
#     : setup_timing_check
#     | hold_timing_check
#     | setuphold_timing_check
#     | recovery_timing_check
#     | removal_timing_check
#     | recrem_timing_check
#     | skew_timing_check
#     | timeskew_timing_check
#     | fullskew_timing_check
#     | period_timing_check
#     | width_timing_check
#     | nochange_timing_check
#     ;

import random

def gen_system_timing_check(depth=3):
    options = [
        gen_setup_timing_check,
        gen_hold_timing_check,
        gen_setuphold_timing_check,
        gen_recovery_timing_check,
        gen_removal_timing_check,
        gen_recrem_timing_check,
        gen_skew_timing_check,
        gen_timeskew_timing_check,
        gen_fullskew_timing_check,
        gen_period_timing_check,
        gen_width_timing_check,
        gen_nochange_timing_check,
    ]
    return random.choice(options)(depth-1)


# setup_timing_check
#     : '$setup' '(' data_event ',' reference_event ',' timing_check_limit notifier_opt? ')' ';'
#     ;

# notifier_opt
#     : ',' notifier?
#     ;

# hold_timing_check
#     : '$hold' '(' reference_event ',' data_event ',' timing_check_limit notifier_opt? ')' ';'
#     ;

# setuphold_timing_check
#     : '$setuphold' '(' reference_event ',' data_event ',' timing_check_limit ',' timing_check_limit timing_check_opt? ')' ';'
#     ;

# timing_check_opt
#     : ',' notifier? stamptime_cond_opt?
#     ;

import random

def gen_setup_timing_check(depth=3):
    """生成符合 setup_timing_check 规则的字符串"""
    result = f"$setup({gen_data_event(depth-1)}, {gen_reference_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 随机决定是否包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    result += ");"
    return result

def gen_notifier_opt(depth=3):
    """生成符合 notifier_opt 规则的字符串"""
    if random.choice([True, False]):  # 50% 机会有 notifier
        return f", {gen_notifier(depth-1)}"
    return ""

def gen_hold_timing_check(depth=3):
    """生成符合 hold_timing_check 规则的字符串"""
    result = f"$hold({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 随机决定是否包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    result += ");"
    return result

def gen_setuphold_timing_check(depth=3):
    """生成符合 setuphold_timing_check 规则的字符串"""
    result = f"$setuphold({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 随机决定是否包含 timing_check_opt
        result += gen_timing_check_opt(depth-1)
    result += ");"
    return result

def gen_timing_check_opt(depth=3):
    """生成符合 timing_check_opt 规则的字符串"""
    result = ""
    if random.choice([True, False]):  # 50% 可能包含 notifier
        result += f", {gen_notifier(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 stamptime_cond_opt
        result += gen_stamptime_cond_opt(depth-1)
    return result


# stamptime_cond_opt
#     : ',' stamptime_condition? checktime_cond_opt?
#     ;

# checktime_cond_opt
#     : ',' checktime_condition? delayed_ref_opt?
#     ;

# delayed_ref_opt
#     : ',' delayed_reference? delayed_data_opt?
#     ;

# delayed_data_opt
#     : ',' delayed_data?
#     ;

def gen_stamptime_cond_opt(depth=3):
    """生成符合 stamptime_cond_opt 规则的字符串"""
    result = ""
    if random.choice([True, False]):  # 50% 可能包含 stamptime_condition
        result += f", {gen_stamptime_condition(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 checktime_cond_opt
        result += gen_checktime_cond_opt(depth-1)
    return result

def gen_checktime_cond_opt(depth=3):
    """生成符合 checktime_cond_opt 规则的字符串"""
    result = ""
    if random.choice([True, False]):  # 50% 可能包含 checktime_condition
        result += f", {gen_checktime_condition(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 delayed_ref_opt
        result += gen_delayed_ref_opt(depth-1)
    return result

def gen_delayed_ref_opt(depth=3):
    """生成符合 delayed_ref_opt 规则的字符串"""
    result = ""
    if random.choice([True, False]):  # 50% 可能包含 delayed_reference
        result += f", {gen_delayed_reference(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 delayed_data_opt
        result += gen_delayed_data_opt(depth-1)
    return result

def gen_delayed_data_opt(depth=3):
    """生成符合 delayed_data_opt 规则的字符串"""
    if random.choice([True, False]):  # 50% 可能包含 delayed_data
        return f", {gen_delayed_data(depth-1)}"
    return ""


# recovery_timing_check
#     : '$recovery' '(' reference_event ',' data_event ',' timing_check_limit notifier_opt? ')' ';'
#     ;

# removal_timing_check
#     : '$removal' '(' reference_event ',' data_event ',' timing_check_limit notifier_opt? ')' ';'
#     ;

# recrem_timing_check
#     : '$recrem' '(' reference_event ',' data_event ',' timing_check_limit ',' timing_check_limit timing_check_opt? ')' ';'
#     ;

# skew_timing_check
#     : '$skew' '(' reference_event ',' data_event ',' timing_check_limit notifier_opt? ')' ';'
#     ;

# timeskew_timing_check
#     : '$timeskew' '(' reference_event ',' data_event ',' timing_check_limit skew_timing_check_opt? ')' ';'
#     ;

def gen_recovery_timing_check(depth=3):
    """生成符合 recovery_timing_check 规则的字符串"""
    result = f"$recovery({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    return result + ");"

def gen_removal_timing_check(depth=3):
    """生成符合 removal_timing_check 规则的字符串"""
    result = f"$removal({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    return result + ");"

def gen_recrem_timing_check(depth=3):
    """生成符合 recrem_timing_check 规则的字符串"""
    result = f"$recrem({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 timing_check_opt
        result += gen_timing_check_opt(depth-1)
    return result + ");"

def gen_skew_timing_check(depth=3):
    """生成符合 skew_timing_check 规则的字符串"""
    result = f"$skew({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    return result + ");"

def gen_timeskew_timing_check(depth=3):
    """生成符合 timeskew_timing_check 规则的字符串"""
    result = f"$timeskew({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 skew_timing_check_opt
        result += gen_skew_timing_check_opt(depth-1)
    return result + ");"


# skew_timing_check_opt
#     : ',' notifier? event_based_flag_opt?
#     ;

# event_based_flag_opt
#     : ',' event_based_flag? remain_active_flag_opt?
#     ;

# remain_active_flag_opt
#     : ',' remain_active_flag?
#     ;

# fullskew_timing_check
#     : '$fullskew' '(' reference_event ',' data_event ',' timing_check_limit ',' timing_check_limit skew_timing_check_opt? ')' ';'
#     ;

# period_timing_check
#     : '$period' '(' controlled_reference_event ',' timing_check_limit notifier_opt? ')' ';'
#     ;

# width_timing_check
#     : '$width' '(' controlled_reference_event ',' timing_check_limit threshold_opt? ')' ';'
#     ;

# threshold_opt
#     : ',' threshold (',' notifier)?
#     ;

def gen_skew_timing_check_opt(depth=3):
    """生成符合 skew_timing_check_opt 规则的字符串"""
    result = ","
    if random.choice([True, False]):  # 50% 可能包含 notifier
        result += gen_notifier(depth-1)
    result += gen_event_based_flag_opt(depth-1)
    return result

def gen_event_based_flag_opt(depth=3):
    """生成符合 event_based_flag_opt 规则的字符串"""
    if random.choice([True, False]):  # 50% 可能包含 event_based_flag
        return f", {gen_event_based_flag(depth-1)}" + gen_remain_active_flag_opt(depth-1)
    return ""

def gen_remain_active_flag_opt(depth=3):
    """生成符合 remain_active_flag_opt 规则的字符串"""
    if random.choice([True, False]):  # 50% 可能包含 remain_active_flag
        return f", {gen_remain_active_flag(depth-1)}"
    return ""

def gen_fullskew_timing_check(depth=3):
    """生成符合 fullskew_timing_check 规则的字符串"""
    result = f"$fullskew({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_timing_check_limit(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 skew_timing_check_opt
        result += gen_skew_timing_check_opt(depth-1)
    return result + ");"

def gen_period_timing_check(depth=3):
    """生成符合 period_timing_check 规则的字符串"""
    result = f"$period({gen_controlled_reference_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    return result + ");"

def gen_width_timing_check(depth=3):
    """生成符合 width_timing_check 规则的字符串"""
    result = f"$width({gen_controlled_reference_event(depth-1)}, {gen_timing_check_limit(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 threshold_opt
        result += gen_threshold_opt(depth-1)
    return result + ");"

def gen_threshold_opt(depth=3):
    """生成符合 threshold_opt 规则的字符串"""
    result = f", {gen_threshold(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 notifier
        result += f", {gen_notifier(depth-1)}"
    return result

# nochange_timing_check
#     : '$nochange' '(' reference_event ',' data_event ',' start_edge_offset ',' end_edge_offset notifier_opt? ')' ';'
#     ;

def gen_nochange_timing_check(depth=3):
    """生成符合 nochange_timing_check 规则的字符串"""
    result = f"$nochange({gen_reference_event(depth-1)}, {gen_data_event(depth-1)}, {gen_start_edge_offset(depth-1)}, {gen_end_edge_offset(depth-1)}"
    if random.choice([True, False]):  # 50% 可能包含 notifier_opt
        result += gen_notifier_opt(depth-1)
    return result + ");"


#     checktime_condition
#     : mintypmax_expression
#     ;

# controlled_reference_event
#     : controlled_timing_check_event
#     ;

# data_event
#     : timing_check_event
#     ;

# delayed_data
#     : terminal_identifier ('[' constant_mintypmax_expression ']')?
#     ;

# delayed_reference
#     : terminal_identifier ('[' constant_mintypmax_expression ']')?
#     ;

# end_edge_offset
#     : mintypmax_expression
#     ;


def gen_checktime_condition(depth=3):
    """生成符合 checktime_condition 规则的字符串"""
    return gen_mintypmax_expression(depth-1)

def gen_controlled_reference_event(depth=3):
    """生成符合 controlled_reference_event 规则的字符串"""
    return gen_controlled_timing_check_event(depth-1)

def gen_data_event(depth=3):
    """生成符合 data_event 规则的字符串"""
    return gen_timing_check_event(depth-1)

def gen_delayed_data(depth=3):
    """生成符合 delayed_data 规则的字符串"""
    result = gen_terminal_identifier(depth-1)
    if random.choice([True, False]):  # 随机决定是否添加可选部分
        result += f"[{gen_constant_mintypmax_expression(depth-1)}]"
    return result

def gen_delayed_reference(depth=3):
    """生成符合 delayed_reference 规则的字符串"""
    result = gen_terminal_identifier(depth-1)
    if random.choice([True, False]):  # 随机决定是否添加可选部分
        result += f"[{gen_constant_mintypmax_expression(depth-1)}]"
    return result

def gen_end_edge_offset(depth=3):
    """生成符合 end_edge_offset 规则的字符串"""
    return gen_mintypmax_expression(depth-1)


# event_based_flag
#     : constant_expression
#     ;

# notifier
#     : variable_identifier
#     ;

# reference_event
#     : timing_check_event
#     ;

# remain_active_flag
#     : constant_expression
#     ;

# stamptime_condition
#     : mintypmax_expression
#     ;

# start_edge_offset
#     : mintypmax_expression
#     ;

# threshold
#     : constant_expression
#     ;

# timing_check_limit
#     : expression
#     ;

def gen_event_based_flag(depth=3):
    """生成符合 event_based_flag 规则的字符串"""
    return gen_constant_expression(depth-1)

def gen_notifier(depth=3):
    """生成符合 notifier 规则的字符串"""
    return gen_variable_identifier(depth-1)

def gen_reference_event(depth=3):
    """生成符合 reference_event 规则的字符串"""
    return gen_timing_check_event(depth-1)

def gen_remain_active_flag(depth=3):
    """生成符合 remain_active_flag 规则的字符串"""
    return gen_constant_expression(depth-1)

def gen_stamptime_condition(depth=3):
    """生成符合 stamptime_condition 规则的字符串"""
    return gen_mintypmax_expression(depth-1)

def gen_start_edge_offset(depth=3):
    """生成符合 start_edge_offset 规则的字符串"""
    return gen_mintypmax_expression(depth-1)

def gen_threshold(depth=3):
    """生成符合 threshold 规则的字符串"""
    return gen_constant_expression(depth-1)

def gen_timing_check_limit(depth=3):
    """生成符合 timing_check_limit 规则的字符串"""
    return gen_expression(depth-1)


# timing_check_event
#     : timing_check_event_control? specify_terminal_descriptor ('&&&' timing_check_condition)?
#     ;

# controlled_timing_check_event
#     : timing_check_event_control specify_terminal_descriptor ('&&&' timing_check_condition)?
#     ;

# timing_check_event_control
#     : 'posedge'
#     | 'negedge'
#     | edge_control_specifier
#     ;

# specify_terminal_descriptor
#     : specify_input_terminal_descriptor
#     | specify_output_terminal_descriptor
#     ;

# edge_control_specifier
#     : 'edge' '[' edge_descriptor (',' edge_descriptor)* ']'
#     ;

# edge_descriptor
#     : EDGE_DESCRIPTOR
#     ;

# timing_check_condition
#     : scalar_timing_check_condition
#     | '(' scalar_timing_check_condition ')'
#     ;


import random

def gen_timing_check_event(depth=3):
    """
    timing_check_event :
         timing_check_event_control? specify_terminal_descriptor ('&&&' timing_check_condition)?
    """
    parts = []
    if random.choice([True, False]):
        parts.append(gen_timing_check_event_control(depth-1))
    parts.append(gen_specify_terminal_descriptor(depth-1))
    if random.choice([True, False]):
        parts.append("&&&")
        parts.append(gen_timing_check_condition(depth-1))
    return " ".join(parts)

def gen_controlled_timing_check_event(depth=3):
    """
    controlled_timing_check_event :
         timing_check_event_control specify_terminal_descriptor ('&&&' timing_check_condition)?
    """
    parts = []
    parts.append(gen_timing_check_event_control(depth-1))
    parts.append(gen_specify_terminal_descriptor(depth-1))
    if random.choice([True, False]):
        parts.append("&&&")
        parts.append(gen_timing_check_condition(depth-1))
    return " ".join(parts)

def gen_timing_check_event_control(depth=3):
    """
    timing_check_event_control :
         'posedge'
       | 'negedge'
       | edge_control_specifier
    """
    option = random.choice(["posedge", "negedge", "edge_control_specifier"])
    if option == "edge_control_specifier":
        return gen_edge_control_specifier(depth-1)
    return option

def gen_specify_terminal_descriptor(depth=3):
    """
    specify_terminal_descriptor :
         specify_input_terminal_descriptor
       | specify_output_terminal_descriptor
    """
    return random.choice([
        gen_specify_input_terminal_descriptor(depth-1),
        gen_specify_output_terminal_descriptor(depth-1)
    ])

def gen_edge_control_specifier(depth=3):
    """
    edge_control_specifier :
         'edge' '[' edge_descriptor (',' edge_descriptor)* ']'
    """
    descriptors = [gen_edge_descriptor(depth-1)]
    for _ in range(random.randint(0, 3)):
        descriptors.append(gen_edge_descriptor(depth-1))
    return "edge [" + ", ".join(descriptors) + "]"

def gen_edge_descriptor(depth=3):
    """
    edge_descriptor :
         EDGE_DESCRIPTOR
    """
    return gen_EDGE_DESCRIPTOR(depth-1)  # 假设该函数已实现

def gen_timing_check_condition(depth=3):
    """
    timing_check_condition :
         scalar_timing_check_condition
       | '(' scalar_timing_check_condition ')'
    """
    condition = gen_scalar_timing_check_condition(depth-1)
    if random.choice([True, False]):
        return condition
    else:
        return "(" + condition + ")"

def gen_scalar_timing_check_condition(depth=3):
    return gen_scalar_timing_check_condition(depth-1)  # 假设该函数已实现


# scalar_timing_check_condition
#     : expression
#     | '~' expression
#     | expression '==' scalar_constant
#     | expression '===' scalar_constant
#     | expression '!=' scalar_constant
#     | expression '!==' scalar_constant
#     ;

# scalar_constant
#     : binary_number
#     | unsigned_number
#     ;


import random

def gen_scalar_timing_check_condition(depth=3):
    option = random.randint(1, 6)
    if option == 1:
        # expression
        return gen_expression(depth-1)
    elif option == 2:
        # '~' expression
        return "~ " + gen_expression(depth-1)
    elif option == 3:
        # expression '==' scalar_constant
        return gen_expression(depth-1) + " == " + gen_scalar_constant(depth-1)
    elif option == 4:
        # expression '===' scalar_constant
        return gen_expression(depth-1) + " === " + gen_scalar_constant(depth-1)
    elif option == 5:
        # expression '!=' scalar_constant
        return gen_expression(depth-1) + " != " + gen_scalar_constant(depth-1)
    else:
        # expression '!==' scalar_constant
        return gen_expression(depth-1) + " !== " + gen_scalar_constant(depth-1)

def gen_scalar_constant(depth=3):
    if random.choice([True, False]):
        return gen_binary_number(depth-1)
    else:
        return gen_unsigned_number(depth-1)


# concatenation
#     : '{' expression (',' expression)* '}'
#     ;

# constant_concatenation
#     : '{' constant_expression (',' constant_expression)* '}'
#     ;

# constant_multiple_concatenation
#     : '{' constant_expression constant_concatenation '}'
#     ;

# module_path_concatenation
#     : '{' module_path_expression (',' module_path_expression)* '}'
#     ;

# module_path_multiple_concatenation
#     : '{' constant_expression module_path_concatenation '}'
#     ;

# multiple_concatenation
#     : '{' constant_expression concatenation '}'
#     ;


import random

def gen_concatenation(depth=3):
    """
    concatenation
        : '{' expression (',' expression)* '}'
    """
    expressions = [gen_expression(depth-1)]
    for _ in range(random.randint(0, 3)):  # Randomly add 0 to 3 more expressions
        expressions.append(gen_expression(depth-1))
    return "{" + ", ".join(expressions) + "}"

def gen_constant_concatenation(depth=3):
    """
    constant_concatenation
        : '{' constant_expression (',' constant_expression)* '}'
    """
    expressions = [gen_constant_expression(depth-1)]
    for _ in range(random.randint(0, 3)):  # Randomly add 0 to 3 more constant expressions
        expressions.append(gen_constant_expression(depth-1))
    return "{" + ", ".join(expressions) + "}"

def gen_constant_multiple_concatenation(depth=3):
    """
    constant_multiple_concatenation
        : '{' constant_expression constant_concatenation '}'
    """
    return "{" + gen_constant_expression(depth-1) + " " + gen_constant_concatenation(depth-1) + "}"

def gen_module_path_concatenation(depth=3):
    """
    module_path_concatenation
        : '{' module_path_expression (',' module_path_expression)* '}'
    """
    expressions = [gen_module_path_expression(depth-1)]
    for _ in range(random.randint(0, 3)):  # Randomly add 0 to 3 more module path expressions
        expressions.append(gen_module_path_expression(depth-1))
    return "{" + ", ".join(expressions) + "}"

def gen_module_path_multiple_concatenation(depth=3):
    """
    module_path_multiple_concatenation
        : '{' constant_expression module_path_concatenation '}'
    """
    return "{" + gen_constant_expression(depth-1) + " " + gen_module_path_concatenation(depth-1) + "}"

def gen_multiple_concatenation(depth=3):
    """
    multiple_concatenation
        : '{' constant_expression concatenation '}'
    """
    return "{" + gen_constant_expression(depth-1) + " " + gen_concatenation(depth-1) + "}"


# constant_function_call
#     : function_identifier attribute_instance* '(' constant_expression (',' constant_expression)* ')'
#     ;

# constant_system_function_call
#     : system_function_identifier '(' constant_expression (',' constant_expression)* ')'
#     ;

# function_call
#     : hierarchical_identifier attribute_instance* '(' expression (',' expression)* ')'
#     ;

# system_function_call
#     : system_function_identifier sys_func_call_port_list?
#     ;

# sys_func_call_port_list
#     : '(' expression (',' expression)* ')'
#     ;

import random

def gen_constant_function_call(depth=3):
    """
    constant_function_call
        : function_identifier attribute_instance* '(' constant_expression (',' constant_expression)* ')'
    """
    # Generate the required components
    function_id = gen_function_identifier(depth-1)
    attribute_instances = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
    constant_expressions = [gen_constant_expression(depth-1)]
    constant_expressions += [gen_constant_expression(depth-1) for _ in range(random.randint(0, 3))]
    # Assemble the function call
    return f"{function_id} {attribute_instances} ({', '.join(constant_expressions)})".strip()

def gen_constant_system_function_call(depth=3):
    """
    constant_system_function_call
        : system_function_identifier '(' constant_expression (',' constant_expression)* ')'
    """
    # Generate the required components
    system_function_id = gen_system_function_identifier(depth-1)
    constant_expressions = [gen_constant_expression(depth-1)]
    constant_expressions += [gen_constant_expression(depth-1) for _ in range(random.randint(0, 3))]
    # Assemble the system function call
    return f"{system_function_id} ({', '.join(constant_expressions)})"

def gen_function_call(depth=3):
    """
    function_call
        : hierarchical_identifier attribute_instance* '(' expression (',' expression)* ')'
    """
    # Generate the required components
    hierarchical_id = gen_hierarchical_identifier(depth-1)
    attribute_instances = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
    expressions = [gen_expression(depth-1)]
    expressions += [gen_expression(depth-1) for _ in range(random.randint(0, 3))]
    # Assemble the function call
    return f"{hierarchical_id} {attribute_instances} ({', '.join(expressions)})".strip()

def gen_system_function_call(depth=3):
    """
    system_function_call
        : system_function_identifier sys_func_call_port_list?
    """
    # Generate the required components
    system_function_id = gen_system_function_identifier(depth-1)
    if random.choice([True, False]):
        sys_func_port_list = gen_sys_func_call_port_list(depth-1)
        return f"{system_function_id} {sys_func_port_list}"
    else:
        return system_function_id

def gen_sys_func_call_port_list(depth=3):
    """
    sys_func_call_port_list
        : '(' expression (',' expression)* ')'
    """
    # Generate the required components
    expressions = [gen_expression(depth-1)]
    expressions += [gen_expression(depth-1) for _ in range(random.randint(0, 3))]
    # Assemble the port list
    return f"({', '.join(expressions)})"


# base_expression
#     : expression
#     ;

# constant_base_expression
#     : constant_expression
#     ;

def gen_base_expression(depth=3):
    """
    base_expression
        : expression
    """
    return gen_expression(depth-1)

def gen_constant_base_expression(depth=3):
    """
    constant_base_expression
        : constant_expression
    """
    return gen_constant_expression(depth-1)


# constant_expression
#     : constant_primary
#     | unary_operator attribute_instance* constant_primary
#     | constant_expression '**' attribute_instance* constant_expression
#     | constant_expression ('*' | '/' | '%') attribute_instance* constant_expression
#     | constant_expression ( '+' | '-') attribute_instance* constant_expression
#     | constant_expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* constant_expression
#     | constant_expression ('<' | '<=' | '>' | '>=') attribute_instance* constant_expression
#     | constant_expression ('==' | '!=' | '===' | '!==') attribute_instance* constant_expression
#     | constant_expression '&' attribute_instance* constant_expression
#     | constant_expression ('^' | '^~' | '~^') attribute_instance* constant_expression
#     | constant_expression '|' attribute_instance* constant_expression
#     | constant_expression '&&' attribute_instance* constant_expression
#     | constant_expression '||' attribute_instance* constant_expression
#     | <assoc = right> constant_expression '?' attribute_instance* constant_expression ':' constant_expression
#     ;


import random

'''
def gen_constant_expression(depth=3):
    """
    constant_expression :
        constant_primary
        | unary_operator attribute_instance* constant_primary
        | constant_expression '**' attribute_instance* constant_expression
        | constant_expression ('*' | '/' | '%') attribute_instance* constant_expression
        | constant_expression ('+' | '-') attribute_instance* constant_expression
        | constant_expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* constant_expression
        | constant_expression ('<' | '<=' | '>' | '>=') attribute_instance* constant_expression
        | constant_expression ('==' | '!=' | '===' | '!==') attribute_instance* constant_expression
        | constant_expression '&' attribute_instance* constant_expression
        | constant_expression ('^' | '^~' | '~^') attribute_instance* constant_expression
        | constant_expression '|' attribute_instance* constant_expression
        | constant_expression '&&' attribute_instance* constant_expression
        | constant_expression '||' attribute_instance* constant_expression
        | <assoc = right> constant_expression '?' attribute_instance* constant_expression ':' constant_expression
    """
    """生成符合 constant_expression 规则的字符串，递归深度受 depth 控制"""
    if depth <= 0:
        return gen_constant_primary(depth-1)  # 递归终止条件，只生成基本表达式
    option = random.randint(1, 14)
    if option == 1:
        # constant_primary
        return gen_constant_primary(depth-1)
    elif option == 2:
        # unary_operator attribute_instance* constant_primary
        unary_op = gen_unary_operator(depth-1)
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{unary_op} {attributes} {gen_constant_primary(depth-1)}".strip()
    elif option == 3:
        # constant_expression '**' attribute_instance* constant_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} ** {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 4:
        # constant_expression ('*' | '/' | '%') attribute_instance* constant_expression
        operator = random.choice(['*', '/', '%'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 5:
        # constant_expression ('+' | '-') attribute_instance* constant_expression
        operator = random.choice(['+', '-'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 6:
        # constant_expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* constant_expression
        operator = random.choice(['>>', '<<', '>>>', '<<<'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 7:
        # constant_expression ('<' | '<=' | '>' | '>=') attribute_instance* constant_expression
        operator = random.choice(['<', '<=', '>', '>='])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 8:
        # constant_expression ('==' | '!=' | '===' | '!==') attribute_instance* constant_expression
        operator = random.choice(['==', '!=', '===', '!=='])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 9:
        # constant_expression '&' attribute_instance* constant_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} & {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 10:
        # constant_expression ('^' | '^~' | '~^') attribute_instance* constant_expression
        operator = random.choice(['^', '^~', '~^'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 11:
        # constant_expression '|' attribute_instance* constant_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} | {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 12:
        # constant_expression '&&' attribute_instance* constant_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} && {attributes} {gen_constant_expression(depth-1)}".strip()
    elif option == 13:
        # constant_expression '||' attribute_instance* constant_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} || {attributes} {gen_constant_expression(depth-1)}".strip()
    else:
        # constant_expression '?' attribute_instance* constant_expression ':' constant_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_constant_expression(depth-1)} ? {attributes} {gen_constant_expression(depth-1)} : {gen_constant_expression(depth-1)}".strip()
'''


def gen_constant_expression(depth=3):
    if depth <= 0 or random.random() < 0.3:  # 30% 概率直接返回基本表达式
        return gen_constant_primary(depth-1)

    option = random.choices(
        population=list(range(1, 15)),  # 14 种可能
        weights=[3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],  # 基本表达式权重较高
        k=1
    )[0]

    if option == 1:
        return gen_constant_primary(depth-1)
    elif option == 2:
        unary_op = gen_unary_operator(depth-1)
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 2))])
        return f"{unary_op} {attributes} {gen_constant_primary(depth-1)}".strip()
    else:
        operator = random.choice(['+', '-', '*', '/', '&&', '||', '?'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 2))])
        return f"{gen_constant_expression(depth-1)} {operator} {attributes} {gen_constant_expression(depth-1)}".strip()




# constant_mintypmax_expression
#     : constant_expression (':' constant_expression ':' constant_expression)?
#     ;

# constant_range_expression
#     : constant_expression
#     | msb_constant_expression ':' lsb_constant_expression
#     | constant_base_expression '+:' width_constant_expression
#     | constant_base_expression '-:' width_constant_expression
#     ;

# dimension_constant_expression
#     : constant_expression
#     ;

def gen_constant_mintypmax_expression(depth=3):
    """
    constant_mintypmax_expression :
        constant_expression (':' constant_expression ':' constant_expression)?
    """
    base_expr = gen_constant_expression(depth-1)
    if random.choice([True, False]):
        mid_expr = gen_constant_expression(depth-1)
        end_expr = gen_constant_expression(depth-1)
        return f"{base_expr} : {mid_expr} : {end_expr}"
    return base_expr

'''
def gen_constant_range_expression(depth=3):
    """
    constant_range_expression :
        constant_expression
        | msb_constant_expression ':' lsb_constant_expression
        | constant_base_expression '+:' width_constant_expression
        | constant_base_expression '-:' width_constant_expression
    """
    option = random.randint(1, 4)
    if option == 1:
        # constant_expression
        return gen_constant_expression(depth-1)
    elif option == 2:
        # msb_constant_expression ':' lsb_constant_expression
        msb_expr = gen_msb_constant_expression(depth-1)
        lsb_expr = gen_lsb_constant_expression(depth-1)
        return f"{msb_expr} : {lsb_expr}"
    elif option == 3:
        # constant_base_expression '+:' width_constant_expression
        base_expr = gen_constant_base_expression(depth-1)
        width_expr = gen_width_constant_expression(depth-1)
        return f"{base_expr} +: {width_expr}"
    else:
        # constant_base_expression '-:' width_constant_expression
        base_expr = gen_constant_base_expression(depth-1)
        width_expr = gen_width_constant_expression(depth-1)
        return f"{base_expr} -: {width_expr}"
'''

def gen_constant_range_expression(depth=3):
    """
    生成符合 constant_range_expression 规则的字符串，并限制递归深度
    """
    if depth <= 0:
        return str(random.randint(0, 15))  # 递归终止，返回简单数值

    option = random.choices(
        population=[1, 2, 3, 4],
        weights=[2, 3, 3, 3],  # 降低 constant_expression 的选择概率
        k=1
    )[0]

    if option == 1:
        # constant_expression
        return gen_constant_expression(depth - 1)
    elif option == 2:
        # msb_constant_expression ':' lsb_constant_expression
        msb_expr = gen_msb_constant_expression(depth - 1)
        lsb_expr = gen_lsb_constant_expression(depth - 1)
        return f"{msb_expr} : {lsb_expr}"
    elif option == 3:
        # constant_base_expression '+:' width_constant_expression
        base_expr = gen_constant_base_expression(depth - 1)
        width_expr = gen_width_constant_expression(depth - 1)
        return f"{base_expr} +: {width_expr}"
    else:
        # constant_base_expression '-:' width_constant_expression
        base_expr = gen_constant_base_expression(depth - 1)
        width_expr = gen_width_constant_expression(depth - 1)
        return f"{base_expr} -: {width_expr}"


def gen_dimension_constant_expression(depth=3):
    """
    dimension_constant_expression :
        constant_expression
    """
    return gen_constant_expression(depth-1)


# expression
#     : primary
#     | unary_operator attribute_instance* primary
#     | expression '**' attribute_instance* expression
#     | expression ( '*' | '/' | '%') attribute_instance* expression
#     | expression ( '+' | '-') attribute_instance* expression
#     | expression ( '>>' | '<<' | '>>>' | '<<<') attribute_instance* expression
#     | expression ( '<' | '<=' | '>' | '>=') attribute_instance* expression
#     | expression ( '==' | '!=' | '===' | '!==') attribute_instance* expression
#     | expression '&' attribute_instance* expression
#     | expression ( '^' | '^~' | '~^') attribute_instance* expression
#     | expression '|' attribute_instance* expression
#     | expression '&&' attribute_instance* expression
#     | expression '||' attribute_instance* expression
#     | <assoc = right> expression '?' attribute_instance* expression ':' expression
#     ;

import random

'''
def gen_expression(depth=3):
    """
    expression :
        primary
        | unary_operator attribute_instance* primary
        | expression '**' attribute_instance* expression
        | expression ('*' | '/' | '%') attribute_instance* expression
        | expression ('+' | '-') attribute_instance* expression
        | expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* expression
        | expression ('<' | '<=' | '>' | '>=') attribute_instance* expression
        | expression ('==' | '!=' | '===' | '!==') attribute_instance* expression
        | expression '&' attribute_instance* expression
        | expression ('^' | '^~' | '~^') attribute_instance* expression
        | expression '|' attribute_instance* expression
        | expression '&&' attribute_instance* expression
        | expression '||' attribute_instance* expression
        | <assoc = right> expression '?' attribute_instance* expression ':' expression
    """
    option = random.randint(1, 14)
    if option == 1:
        # primary
        return gen_primary(depth-1)
    elif option == 2:
        # unary_operator attribute_instance* primary
        unary_op = gen_unary_operator(depth-1)
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{unary_op} {attributes} {gen_primary(depth-1)}".strip()
    elif option == 3:
        # expression '**' attribute_instance* expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} ** {attributes} {gen_expression(depth-1)}".strip()
    elif option == 4:
        # expression ('*' | '/' | '%') attribute_instance* expression
        operator = random.choice(['*', '/', '%'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 5:
        # expression ('+' | '-') attribute_instance* expression
        operator = random.choice(['+', '-'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 6:
        # expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* expression
        operator = random.choice(['>>', '<<', '>>>', '<<<'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 7:
        # expression ('<' | '<=' | '>' | '>=') attribute_instance* expression
        operator = random.choice(['<', '<=', '>', '>='])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 8:
        # expression ('==' | '!=' | '===' | '!==') attribute_instance* expression
        operator = random.choice(['==', '!=', '===', '!=='])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 9:
        # expression '&' attribute_instance* expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} & {attributes} {gen_expression(depth-1)}".strip()
    elif option == 10:
        # expression ('^' | '^~' | '~^') attribute_instance* expression
        operator = random.choice(['^', '^~', '~^'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 11:
        # expression '|' attribute_instance* expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} | {attributes} {gen_expression(depth-1)}".strip()
    elif option == 12:
        # expression '&&' attribute_instance* expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} && {attributes} {gen_expression(depth-1)}".strip()
    elif option == 13:
        # expression '||' attribute_instance* expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} || {attributes} {gen_expression(depth-1)}".strip()
    else:
        # expression '?' attribute_instance* expression ':' expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_expression(depth-1)} ? {attributes} {gen_expression(depth-1)} : {gen_expression(depth-1)}".strip()
'''

def gen_expression(depth=3):
    """
    生成符合 expression 规则的字符串，并限制递归深度
    expression :
        primary
        | unary_operator attribute_instance* primary
        | expression '**' attribute_instance* expression
        | expression ('*' | '/' | '%') attribute_instance* expression
        | expression ('+' | '-') attribute_instance* expression
        | expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* expression
        | expression ('<' | '<=' | '>' | '>=') attribute_instance* expression
        | expression ('==' | '!=' | '===' | '!==') attribute_instance* expression
        | expression '&' attribute_instance* expression
        | expression ('^' | '^~' | '~^') attribute_instance* expression
        | expression '|' attribute_instance* expression
        | expression '&&' attribute_instance* expression
        | expression '||' attribute_instance* expression
        | expression '?' attribute_instance* expression ':' expression
    """
    # 当深度耗尽时直接返回一个基本表达式，防止进一步递归
    if depth <= 0:
        return gen_primary(depth-1)

    option = random.randint(1, 14)
    if option == 1:
        # primary
        return gen_primary(depth-1)
    elif option == 2:
        # unary_operator attribute_instance* primary
        unary_op = gen_unary_operator(depth-1)
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{unary_op} {attributes} {gen_primary(depth-1)}".strip()
    elif option == 3:
        # expression '**' attribute_instance* expression
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} ** {attributes} {gen_expression(depth-1)}".strip()
    elif option == 4:
        # expression ('*' | '/' | '%') attribute_instance* expression
        operator = random.choice(['*', '/', '%'])
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 5:
        # expression ('+' | '-') attribute_instance* expression
        operator = random.choice(['+', '-'])
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 6:
        # expression ('>>' | '<<' | '>>>' | '<<<') attribute_instance* expression
        operator = random.choice(['>>', '<<', '>>>', '<<<'])
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 7:
        # expression ('<' | '<=' | '>' | '>=') attribute_instance* expression
        operator = random.choice(['<', '<=', '>', '>='])
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 8:
        # expression ('==' | '!=' | '===' | '!==') attribute_instance* expression
        operator = random.choice(['==', '!=', '===', '!=='])
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 9:
        # expression '&' attribute_instance* expression
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} & {attributes} {gen_expression(depth-1)}".strip()
    elif option == 10:
        # expression ('^' | '^~' | '~^') attribute_instance* expression
        operator = random.choice(['^', '^~', '~^'])
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} {operator} {attributes} {gen_expression(depth-1)}".strip()
    elif option == 11:
        # expression '|' attribute_instance* expression
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} | {attributes} {gen_expression(depth-1)}".strip()
    elif option == 12:
        # expression '&&' attribute_instance* expression
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} && {attributes} {gen_expression(depth-1)}".strip()
    elif option == 13:
        # expression '||' attribute_instance* expression
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} || {attributes} {gen_expression(depth-1)}".strip()
    else:
        # expression '?' attribute_instance* expression ':' expression
        attributes = " ".join(gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3)))
        return f"{gen_expression(depth-1)} ? {attributes} {gen_expression(depth-1)} : {gen_expression(depth-1)}".strip()


# lsb_constant_expression
#     : constant_expression
#     ;

# mintypmax_expression
#     : expression (':' expression ':' expression)?
#     ;

def gen_lsb_constant_expression(depth=3):
    """
    lsb_constant_expression :
        constant_expression
    """
    return gen_constant_expression(depth-1)

def gen_mintypmax_expression(depth=3):
    """
    mintypmax_expression :
        expression (':' expression ':' expression)?
    """
    base_expr = gen_expression(depth-1)
    if random.choice([True, False]):
        mid_expr = gen_expression(depth-1)
        end_expr = gen_expression(depth-1)
        return f"{base_expr} : {mid_expr} : {end_expr}"
    return base_expr


# module_path_expression
#     : module_path_primary
#     | unary_module_path_operator attribute_instance* module_path_primary
#     | module_path_expression ('==' | '!=') attribute_instance* module_path_expression
#     | module_path_expression '&' attribute_instance* module_path_expression
#     | module_path_expression ('^' | '^~' | '~^') attribute_instance* module_path_expression
#     | module_path_expression '|' attribute_instance* module_path_expression
#     | module_path_expression '&&' attribute_instance* module_path_expression
#     | module_path_expression '||' attribute_instance* module_path_expression
#     | <assoc = right> module_path_expression '?' attribute_instance* module_path_expression ':' module_path_expression
#     ;

def gen_module_path_expression(depth=3):
    """
    module_path_expression :
        module_path_primary
        | unary_module_path_operator attribute_instance* module_path_primary
        | module_path_expression ('==' | '!=') attribute_instance* module_path_expression
        | module_path_expression '&' attribute_instance* module_path_expression
        | module_path_expression ('^' | '^~' | '~^') attribute_instance* module_path_expression
        | module_path_expression '|' attribute_instance* module_path_expression
        | module_path_expression '&&' attribute_instance* module_path_expression
        | module_path_expression '||' attribute_instance* module_path_expression
        | <assoc = right> module_path_expression '?' attribute_instance* module_path_expression ':' module_path_expression
    """
    option = random.randint(1, 9)
    if option == 1:
        # module_path_primary
        return gen_module_path_primary(depth-1)
    elif option == 2:
        # unary_module_path_operator attribute_instance* module_path_primary
        unary_op = gen_unary_module_path_operator(depth-1)
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{unary_op} {attributes} {gen_module_path_primary(depth-1)}".strip()
    elif option == 3:
        # module_path_expression ('==' | '!=') attribute_instance* module_path_expression
        operator = random.choice(['==', '!='])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} {operator} {attributes} {gen_module_path_expression(depth-1)}".strip()
    elif option == 4:
        # module_path_expression '&' attribute_instance* module_path_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} & {attributes} {gen_module_path_expression(depth-1)}".strip()
    elif option == 5:
        # module_path_expression ('^' | '^~' | '~^') attribute_instance* module_path_expression
        operator = random.choice(['^', '^~', '~^'])
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} {operator} {attributes} {gen_module_path_expression(depth-1)}".strip()
    elif option == 6:
        # module_path_expression '|' attribute_instance* module_path_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} | {attributes} {gen_module_path_expression(depth-1)}".strip()
    elif option == 7:
        # module_path_expression '&&' attribute_instance* module_path_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} && {attributes} {gen_module_path_expression(depth-1)}".strip()
    elif option == 8:
        # module_path_expression '||' attribute_instance* module_path_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} || {attributes} {gen_module_path_expression(depth-1)}".strip()
    else:
        # module_path_expression '?' attribute_instance* module_path_expression ':' module_path_expression
        attributes = " ".join([gen_attribute_instance(depth-1) for _ in range(random.randint(0, 3))])
        return f"{gen_module_path_expression(depth-1)} ? {attributes} {gen_module_path_expression(depth-1)} : {gen_module_path_expression(depth-1)}".strip()



# module_path_mintypmax_expression
#     : module_path_expression (':' module_path_expression ':' module_path_expression)?
#     ;

# msb_constant_expression
#     : constant_expression
#     ;

# range_expression
#     : expression
#     | msb_constant_expression ':' lsb_constant_expression
#     | base_expression '+:' width_constant_expression
#     | base_expression '-:' width_constant_expression
#     ;

# width_constant_expression
#     : constant_expression
#     ;

def gen_module_path_mintypmax_expression(depth=3):
    """
    module_path_mintypmax_expression :
        module_path_expression (':' module_path_expression ':' module_path_expression)?
    """
    base_expr = gen_module_path_expression(depth-1)
    if random.choice([True, False]):
        mid_expr = gen_module_path_expression(depth-1)
        end_expr = gen_module_path_expression(depth-1)
        return f"{base_expr} : {mid_expr} : {end_expr}"
    return base_expr

def gen_msb_constant_expression(depth=3):
    """
    msb_constant_expression :
        constant_expression
    """
    return gen_constant_expression(depth-1)

def gen_range_expression(depth=3):
    """
    range_expression :
        expression
        | msb_constant_expression ':' lsb_constant_expression
        | base_expression '+:' width_constant_expression
        | base_expression '-:' width_constant_expression
    """
    option = random.randint(1, 4)
    if option == 1:
        # expression
        return gen_expression(depth-1)
    elif option == 2:
        # msb_constant_expression ':' lsb_constant_expression
        msb_expr = gen_msb_constant_expression(depth-1)
        lsb_expr = gen_lsb_constant_expression(depth-1)
        return f"{msb_expr} : {lsb_expr}"
    elif option == 3:
        # base_expression '+:' width_constant_expression
        base_expr = gen_base_expression(depth-1)
        width_expr = gen_width_constant_expression(depth-1)
        return f"{base_expr} +: {width_expr}"
    else:
        # base_expression '-:' width_constant_expression
        base_expr = gen_base_expression(depth-1)
        width_expr = gen_width_constant_expression(depth-1)
        return f"{base_expr} -: {width_expr}"

def gen_width_constant_expression(depth=3):
    """
    width_constant_expression :
        constant_expression
    """
    return gen_constant_expression(depth-1)


# constant_primary
#     : number
#     | identifier ( '[' constant_range_expression ']')?
#     | constant_concatenation
#     | constant_multiple_concatenation
#     | constant_function_call
#     | constant_system_function_call
#     | '(' constant_mintypmax_expression ')'
#     | string_
#     ;

# module_path_primary
#     : number
#     | identifier
#     | module_path_concatenation
#     | module_path_multiple_concatenation
#     | function_call
#     | system_function_call
#     | '(' module_path_mintypmax_expression ')'
#     ;

# primary
#     : number
#     | hierarchical_identifier select_?
#     | concatenation
#     | multiple_concatenation
#     | function_call
#     | system_function_call
#     | '(' mintypmax_expression ')'
#     | string_
#     ;

# select_
#     : bit_select? '[' range_expression ']'
#     ;

# bit_select
#     : ('[' expression ']')+
#     ;

'''
def gen_constant_primary(depth=3):
    """
    constant_primary :
        number
        | identifier ('[' constant_range_expression ']')?
        | constant_concatenation
        | constant_multiple_concatenation
        | constant_function_call
        | constant_system_function_call
        | '(' constant_mintypmax_expression ')'
        | string_
    """
    option = random.randint(1, 8)
    if option == 1:
        return gen_number(depth-1)
    elif option == 2:
        identifier = gen_identifier(depth-1)
        if random.choice([True, False]):
            range_expr = gen_constant_range_expression(depth-1)
            return f"{identifier}[{range_expr}]"
        return identifier
    elif option == 3:
        return gen_constant_concatenation(depth-1)
    elif option == 4:
        return gen_constant_multiple_concatenation(depth-1)
    elif option == 5:
        return gen_constant_function_call(depth-1)
    elif option == 6:
        return gen_constant_system_function_call(depth-1)
    elif option == 7:
        return f"({gen_constant_mintypmax_expression(depth-1)})"
    else:
        return gen_string_(depth-1)
'''

def gen_constant_primary(depth=3):
    """
    生成符合 constant_primary 规则的字符串，并限制递归深度
    """
    if depth <= 0:
        return gen_number(depth-1) if random.choice([True, False]) else gen_identifier(depth-1)

    option = random.choices(
        population=[1, 2, 3, 4, 5, 6, 7, 8],
        weights=[3, 3, 2, 2, 1, 1, 2, 2],  # 让简单选项更容易被选中
        k=1
    )[0]

    if option == 1:
        return gen_number(depth-1)
    elif option == 2:
        identifier = gen_identifier(depth-1)
        if random.choice([True, False]):
            range_expr = gen_constant_range_expression(depth - 1)
            return f"{identifier}[{range_expr}]"
        return identifier
    elif option == 3:
        return gen_constant_concatenation(depth - 1)
    elif option == 4:
        return gen_constant_multiple_concatenation(depth - 1)
    elif option == 5:
        return gen_constant_function_call(depth - 1)
    elif option == 6:
        return gen_constant_system_function_call(depth - 1)
    elif option == 7:
        return f"({gen_constant_mintypmax_expression(depth - 1)})"
    else:
        return gen_string_(depth-1)


def gen_module_path_primary(depth=3):
    """
    module_path_primary :
        number
        | identifier
        | module_path_concatenation
        | module_path_multiple_concatenation
        | function_call
        | system_function_call
        | '(' module_path_mintypmax_expression ')'
    """
    option = random.randint(1, 7)
    if option == 1:
        return gen_number(depth-1)
    elif option == 2:
        return gen_identifier(depth-1)
    elif option == 3:
        return gen_module_path_concatenation(depth-1)
    elif option == 4:
        return gen_module_path_multiple_concatenation(depth-1)
    elif option == 5:
        return gen_function_call(depth-1)
    elif option == 6:
        return gen_system_function_call(depth-1)
    else:
        return f"({gen_module_path_mintypmax_expression(depth-1)})"

def gen_primary(depth=3):
    """
    primary :
        number
        | hierarchical_identifier select_?
        | concatenation
        | multiple_concatenation
        | function_call
        | system_function_call
        | '(' mintypmax_expression ')'
        | string_
    """
    option = random.randint(1, 8)
    if option == 1:
        return gen_number(depth-1)
    elif option == 2:
        hierarchical_id = gen_hierarchical_identifier(depth-1)
        if random.choice([True, False]):
            select_part = gen_select_(depth-1)
            return f"{hierarchical_id} {select_part}"
        return hierarchical_id
    elif option == 3:
        return gen_concatenation(depth-1)
    elif option == 4:
        return gen_multiple_concatenation(depth-1)
    elif option == 5:
        return gen_function_call(depth-1)
    elif option == 6:
        return gen_system_function_call(depth-1)
    elif option == 7:
        return f"({gen_mintypmax_expression(depth-1)})"
    else:
        return gen_string_(depth-1)

def gen_select_(depth=3):
    """
    select_ :
        bit_select? '[' range_expression ']'
    """
    if random.choice([True, False]):
        bit_select = gen_bit_select(depth-1)
        range_expr = gen_range_expression(depth-1)
        return f"{bit_select}[{range_expr}]"
    else:
        range_expr = gen_range_expression(depth-1)
        return f"[{range_expr}]"

def gen_bit_select(depth=3):
    """
    bit_select :
        ('[' expression ']')+
    """
    bit_expressions = [f"[{gen_expression(depth-1)}]" for _ in range(random.randint(1, 3))]
    return " ".join(bit_expressions)

# net_lvalue
#     : hierarchical_identifier const_select?
#     | '{' net_lvalue ( ',' net_lvalue)* '}'
#     ;

# const_select
#     : const_bit_select? '[' constant_range_expression ']'
#     ;

# const_bit_select
#     : ('[' constant_expression ']')+
#     ;

# variable_lvalue
#     : hierarchical_identifier select_?
#     | '{' variable_lvalue ( ',' variable_lvalue)* '}'
#     ;

def gen_net_lvalue(depth=3):
    """
    net_lvalue :
        hierarchical_identifier const_select?
        | '{' net_lvalue ( ',' net_lvalue )* '}'
    """
    if random.choice([True, False]):
        # hierarchical_identifier const_select?
        hierarchical_id = gen_hierarchical_identifier(depth-1)
        if random.choice([True, False]):
            const_select = gen_const_select(depth-1)
            return f"{hierarchical_id} {const_select}".strip()
        return hierarchical_id
    else:
        # '{' net_lvalue ( ',' net_lvalue )* '}'
        lvalues = [gen_net_lvalue(depth-1)]
        lvalues.extend([gen_net_lvalue(depth-1) for _ in range(random.randint(0, 3))])  # Randomly add up to 3 more
        return f"{{{', '.join(lvalues)}}}"

def gen_const_select(depth=3):
    """
    const_select :
        const_bit_select? '[' constant_range_expression ']'
    """
    if random.choice([True, False]):
        # const_bit_select '[' constant_range_expression ']'
        const_bit = gen_const_bit_select(depth-1)
        range_expr = gen_constant_range_expression(depth-1)
        return f"{const_bit}[{range_expr}]"
    else:
        # '[' constant_range_expression ']'
        range_expr = gen_constant_range_expression(depth-1)
        return f"[{range_expr}]"

def gen_const_bit_select(depth=3):
    """
    const_bit_select :
        ('[' constant_expression ']')+
    """
    bit_expressions = [f"[{gen_constant_expression(depth-1)}]" for _ in range(random.randint(1, 3))]  # At least 1
    return " ".join(bit_expressions)

def gen_variable_lvalue(depth=3):
    """
    variable_lvalue :
        hierarchical_identifier select_?
        | '{' variable_lvalue ( ',' variable_lvalue )* '}'
    """
    if random.choice([True, False]):
        # hierarchical_identifier select_?
        hierarchical_id = gen_hierarchical_identifier(depth-1)
        if random.choice([True, False]):
            select = gen_select_(depth-1)
            return f"{hierarchical_id} {select}".strip()
        return hierarchical_id
    else:
        # '{' variable_lvalue ( ',' variable_lvalue )* '}'
        lvalues = [gen_variable_lvalue(depth-1)]
        lvalues.extend([gen_variable_lvalue(depth-1) for _ in range(random.randint(0, 3))])  # Randomly add up to 3 more
        return f"{{{', '.join(lvalues)}}}"


# unary_operator
#     : '+'
#     | '-'
#     | '!'
#     | '~'
#     | '&'
#     | '~&'
#     | '|'
#     | '~|'
#     | '^'
#     | '~^'
#     | '^~'
#     ;

# unary_module_path_operator
#     : '!'
#     | '~'
#     | '&'
#     | '~&'
#     | '|'
#     | '~|'
#     | '^'
#     | '~^'
#     | '^~'
#     ;

def gen_unary_operator(depth=3):
    """
    unary_operator :
        '+' | '-' | '!' | '~' | '&' | '~&' | '|' | '~|' | '^' | '~^' | '^~'
    """
    return random.choice(['+', '-', '!', '~', '&', '~&', '|', '~|', '^', '~^', '^~'])

def gen_unary_module_path_operator(depth=3):
    """
    unary_module_path_operator :
        '!' | '~' | '&' | '~&' | '|' | '~|' | '^' | '~^' | '^~'
    """
    return random.choice(['!', '~', '&', '~&', '|', '~|', '^', '~^', '^~'])


# number
#     : decimal_number
#     | octal_number
#     | binary_number
#     | hex_number
#     | real_number
#     ;

# real_number
#     : fixed_point_number
#     | exponential_number
#     ;

# decimal_number
#     : unsigned_number
#     | size? decimal_base decimal_value
#     ;

# binary_number
#     : size? binary_base binary_value
#     ;

# octal_number
#     : size? octal_base octal_value
#     ;

# hex_number
#     : size? hex_base hex_value
#     ;


def gen_number(depth=3):
    """
    number :
        decimal_number
        | octal_number
        | binary_number
        | hex_number
        | real_number
    """
    option = random.randint(1, 5)
    if option == 1:
        return gen_decimal_number(depth-1)
    elif option == 2:
        return gen_octal_number(depth-1)
    elif option == 3:
        return gen_binary_number(depth-1)
    elif option == 4:
        return gen_hex_number(depth-1)
    else:
        return gen_real_number(depth-1)


def gen_real_number(depth=3):
    """
    real_number :
        fixed_point_number
        | exponential_number
    """
    if random.choice([True, False]):
        return gen_fixed_point_number(depth-1)
    else:
        return gen_exponential_number(depth-1)

def gen_decimal_number(depth=3):
    """
    decimal_number :
        unsigned_number
        | size? decimal_base decimal_value
    """
    if random.choice([True, False]):
        return gen_unsigned_number(depth-1)
    else:
        size = gen_size(depth-1) if random.choice([True, False]) else ""
        base = gen_decimal_base(depth-1)
        value = gen_decimal_value(depth-1)
        return f"{size}{base}{value}".strip()

def gen_binary_number(depth=3):
    """
    binary_number :
        size? binary_base binary_value
    """
    size = gen_size(depth-1) if random.choice([True, False]) else ""
    base = gen_binary_base(depth-1)
    value = gen_binary_value(depth-1)
    return f"{size}{base}{value}".strip()

def gen_octal_number(depth=3):
    """
    octal_number :
        size? octal_base octal_value
    """
    size = gen_size(depth-1) if random.choice([True, False]) else ""
    base = gen_octal_base(depth-1)
    value = gen_octal_value(depth-1)
    return f"{size}{base}{value}".strip()

def gen_hex_number(depth=3):
    """
    hex_number :
        size? hex_base hex_value
    """
    size = gen_size(depth-1) if random.choice([True, False]) else ""
    base = gen_hex_base(depth-1)
    value = gen_hex_value(depth-1)
    return f"{size}{base}{value}".strip()


# size
#     : UNSIGNED_NUMBER
#     ;

# fixed_point_number
#     : FIXED_POINT_NUMBER
#     ;

# exponential_number
#     : EXPONENTIAL_NUMBER
#     ;

# unsigned_number
#     : UNSIGNED_NUMBER
#     ;

# decimal_value
#     : UNSIGNED_NUMBER
#     | X_OR_Z_UNDERSCORE
#     ;

# binary_value
#     : BINARY_VALUE
#     ;

# octal_value
#     : OCTAL_VALUE
#     ;

# hex_value
#     : HEX_VALUE
#     ;

# decimal_base
#     : DECIMAL_BASE
#     ;

# binary_base
#     : BINARY_BASE
#     ;

# octal_base
#     : OCTAL_BASE
#     ;

# hex_base
#     : HEX_BASE
#     ;


def gen_size(depth=3):
    """
    size :
        UNSIGNED_NUMBER
    """
    return gen_unsigned_number(depth-1)

def gen_fixed_point_number(depth=3):
    """
    fixed_point_number :
        FIXED_POINT_NUMBER
    """
    return gen_FIXED_POINT_NUMBER(depth-1)  # Assume this function is implemented

def gen_exponential_number(depth=3):
    """
    exponential_number :
        EXPONENTIAL_NUMBER
    """
    return gen_EXPONENTIAL_NUMBER(depth-1)  # Assume this function is implemented

def gen_unsigned_number(depth=3):
    """
    unsigned_number :
        UNSIGNED_NUMBER
    """
    return gen_UNSIGNED_NUMBER(depth-1)  # Assume this function is implemented

def gen_decimal_value(depth=3):
    """
    decimal_value :
        UNSIGNED_NUMBER
        | X_OR_Z_UNDERSCORE
    """
    return random.choice([gen_UNSIGNED_NUMBER(depth-1), gen_X_OR_Z_UNDERSCORE(depth-1)])

def gen_binary_value(depth=3):
    """
    binary_value :
        BINARY_VALUE
    """
    return gen_BINARY_VALUE(depth-1)  # Assume this function is implemented

def gen_octal_value(depth=3):
    """
    octal_value :
        OCTAL_VALUE
    """
    return gen_OCTAL_VALUE(depth-1)  # Assume this function is implemented

def gen_hex_value(depth=3):
    """
    hex_value :
        HEX_VALUE
    """
    return gen_HEX_VALUE(depth-1)  # Assume this function is implemented

def gen_decimal_base(depth=3):
    """
    decimal_base :
        DECIMAL_BASE
    """
    return gen_DECIMAL_BASE(depth-1)  # Assume this function is implemented

def gen_binary_base(depth=3):
    """
    binary_base :
        BINARY_BASE
    """
    return gen_BINARY_BASE(depth-1)  # Assume this function is implemented

def gen_octal_base(depth=3):
    """
    octal_base :
        OCTAL_BASE
    """
    return gen_OCTAL_BASE(depth-1)  # Assume this function is implemented

def gen_hex_base(depth=3):
    """
    hex_base :
        HEX_BASE
    """
    return gen_HEX_BASE(depth-1)  # Assume this function is implemented

# string_
#     : STRING
#     ;

def gen_string_(depth=3):
    """
    string_ :
        STRING
    """
    return gen_STRING(depth-1)  # Assume this function is implemented


# attribute_instance
#     : '(' '*' attr_spec (',' attr_spec)* '*' ')'
#     ;

# attr_spec
#     : attr_name ('=' constant_expression)?
#     ;

# attr_name
#     : identifier
#     ;

def gen_attribute_instance(depth=3):
    """
    attribute_instance :
        '(' '*' attr_spec (',' attr_spec)* '*' ')'
    """
    attr_specs = [gen_attr_spec(depth-1)]
    attr_specs.extend([gen_attr_spec(depth-1) for _ in range(random.randint(0, 3))])  # Randomly add up to 3 more
    return f"(* {', '.join(attr_specs)} *)"

def gen_attr_spec(depth=3):
    """
    attr_spec :
        attr_name ('=' constant_expression)?
    """
    attr_name = gen_attr_name(depth-1)
    if random.choice([True, False]):
        const_expr = gen_constant_expression(depth-1)
        return f"{attr_name} = {const_expr}"
    return attr_name

def gen_attr_name(depth=3): 
    """
    attr_name :
        identifier
    """
    return gen_identifier(depth-1)



# block_identifier
#     : identifier
#     ;

# cell_identifier
#     : identifier
#     ;

# config_identifier
#     : identifier
#     ;

# escaped_identifier
#     : ESCAPED_IDENTIFIER
#     ;

# event_identifier
#     : identifier
#     ;


def gen_block_identifier(depth=3):
    """
    block_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_cell_identifier(depth=3):
    """
    cell_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_config_identifier(depth=3):
    """
    config_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_escaped_identifier(depth=3):
    """
    escaped_identifier :
        ESCAPED_IDENTIFIER
    """
    return gen_ESCAPED_IDENTIFIER(depth-1)  # Assume this function is implemented

def gen_event_identifier(depth=3):
    """
    event_identifier :
        identifier
    """
    return gen_identifier(depth-1)


# function_identifier
#     : identifier
#     ;

# gate_instance_identifier
#     : identifier
#     ;

# generate_block_identifier
#     : identifier
#     ;

# genvar_identifier
#     : identifier
#     ;

# hierarchical_identifier
#     : hier_ref* identifier
#     ;

# hier_ref
#     : identifier const_bit_select? '.'
#     ;

# identifier
#     : escaped_identifier
#     | simple_identifier
#     ;


def gen_function_identifier(depth=3):
    """
    function_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_gate_instance_identifier(depth=3):
    """
    gate_instance_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_generate_block_identifier(depth=3):
    """
    generate_block_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_genvar_identifier(depth=3):
    """
    genvar_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_hierarchical_identifier(depth=3):
    """
    hierarchical_identifier :
        hier_ref* identifier
    """
    hier_refs = " ".join([gen_hier_ref(depth-1) for _ in range(random.randint(0, 3))])  # Randomly generate 0 to 3 hier_refs
    base_identifier = gen_identifier(depth-1)
    return f"{hier_refs} {base_identifier}".strip()

def gen_hier_ref(depth=3):
    """
    hier_ref :
        identifier const_bit_select? '.'
    """
    base_identifier = gen_identifier(depth-1)
    if random.choice([True, False]):
        const_bit_select = gen_const_bit_select(depth-1)
        return f"{base_identifier}{const_bit_select}."
    return f"{base_identifier}."

def gen_identifier(depth=3):
    """
    identifier :
        escaped_identifier
        | simple_identifier
    """
    if random.choice([True, False]):
        return gen_escaped_identifier(depth-1)
    else:
        return gen_simple_identifier(depth-1)



# input_port_identifier
#     : identifier
#     ;

# instance_identifier
#     : identifier
#     ;

# library_identifier
#     : identifier
#     ;

# module_identifier
#     : identifier
#     ;

# module_instance_identifier
#     : identifier
#     ;

# net_identifier
#     : identifier
#     ;

# output_port_identifier
#     : identifier
#     ;


def gen_input_port_identifier(depth=3):
    """
    input_port_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_instance_identifier(depth=3):
    """
    instance_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_library_identifier(depth=3):
    """
    library_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_module_identifier(depth=3):
    """
    module_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_module_instance_identifier(depth=3):
    """
    module_instance_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_net_identifier(depth=3):
    """
    net_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_output_port_identifier(depth=3):
    """
    output_port_identifier :
        identifier
    """
    return gen_identifier(depth-1)


# parameter_identifier
#     : identifier
#     ;

# port_identifier
#     : identifier
#     ;

# real_identifier
#     : identifier
#     ;

# simple_identifier
#     : SIMPLE_IDENTIFIER
#     ;

# specparam_identifier
#     : identifier
#     ;

# system_function_identifier
#     : SYSTEM_TF_IDENTIFIER
#     ;

# system_task_identifier
#     : SYSTEM_TF_IDENTIFIER
#     ;

# task_identifier
#     : identifier
#     ;

# terminal_identifier
#     : identifier
#     ;

def gen_parameter_identifier(depth=3):
    """
    parameter_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_port_identifier(depth=3):
    """
    port_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_real_identifier(depth=3):
    """
    real_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_simple_identifier(depth=3):
    """
    simple_identifier :
        SIMPLE_IDENTIFIER
    """
    return gen_SIMPLE_IDENTIFIER(depth-1)  # Assume this function is implemented

def gen_specparam_identifier(depth=3):
    """
    specparam_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_system_function_identifier(depth=3):
    """
    system_function_identifier :
        SYSTEM_TF_IDENTIFIER
    """
    return gen_SYSTEM_TF_IDENTIFIER(depth-1)  # Assume this function is implemented

def gen_system_task_identifier(depth=3):
    """
    system_task_identifier :
        SYSTEM_TF_IDENTIFIER
    """
    return gen_SYSTEM_TF_IDENTIFIER(depth-1)  # Assume this function is implemented

def gen_task_identifier(depth=3):
    """
    task_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_terminal_identifier(depth=3):
    """
    terminal_identifier :
        identifier
    """
    return gen_identifier(depth-1)


# topmodule_identifier
#     : identifier
#     ;

# udp_identifier
#     : identifier
#     ;

# udp_instance_identifier
#     : identifier
#     ;

# variable_identifier
#     : identifier
#     ;


def gen_topmodule_identifier(depth=3):
    """
    topmodule_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_udp_identifier(depth=3):
    """
    udp_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_udp_instance_identifier(depth=3):
    """
    udp_instance_identifier :
        identifier
    """
    return gen_identifier(depth-1)

def gen_variable_identifier(depth=3):
    """
    variable_identifier :
        identifier
    """
    return gen_identifier(depth-1)


# ALWAYS              : 'always';
# AND                 : 'and';
# ASSIGN              : 'assign';
# AUTOMATIC           : 'automatic';
# BEGIN               : 'begin';
# BUF                 : 'buf';
# BUFIFONE            : 'bufif1';
# BUFIFZERO           : 'bufif0';
# CASE                : 'case';
# CASEX               : 'casex';
# CASEZ               : 'casez';
# CELL                : 'cell';
# CMOS                : 'cmos';
# CONFIG              : 'config';
# DEASSIGN            : 'deassign';
# DEFAULT             : 'default';
# DEFPARAM            : 'defparam';
# DESIGN              : 'design';
# DISABLE             : 'disable';
# DLFULLSKEW          : '$fullskew';
# DLHOLD              : '$hold';
# DLNOCHANGE          : '$nochange';
# DLPERIOD            : '$period';
# DLRECOVERY          : '$recovery';
# DLRECREM            : '$recrem';
# DLREMOVAL           : '$removal';

def gen_ALWAYS(depth=3):
    return "always"

def gen_AND(depth=3):
    return "and"

def gen_ASSIGN(depth=3):
    return "assign"

def gen_AUTOMATIC(depth=3):
    return "automatic"

def gen_BEGIN(depth=3):
    return "begin"

def gen_BUF(depth=3):
    return "buf"

def gen_BUFIFONE(depth=3):
    return "bufif1"

def gen_BUFIFZERO(depth=3):
    return "bufif0"

def gen_CASE(depth=3):
    return "case"

def gen_CASEX(depth=3):
    return "casex"

def gen_CASEZ(depth=3):
    return "casez"

def gen_CELL(depth=3):
    return "cell"

def gen_CMOS(depth=3):
    return "cmos"

def gen_CONFIG(depth=3):
    return "config"

def gen_DEASSIGN(depth=3):
    return "deassign"

def gen_DEFAULT(depth=3):
    return "default"

def gen_DEFPARAM(depth=3):
    return "defparam"

def gen_DESIGN(depth=3):
    return "design"

def gen_DISABLE(depth=3):
    return "disable"

def gen_DLFULLSKEW(depth=3):
    return "$fullskew"

def gen_DLHOLD(depth=3):
    return "$hold"

def gen_DLNOCHANGE(depth=3):
    return "$nochange"

def gen_DLPERIOD(depth=3):
    return "$period"

def gen_DLRECOVERY(depth=3):
    return "$recovery"

def gen_DLRECREM(depth=3):
    return "$recrem"

def gen_DLREMOVAL(depth=3):
    return "$removal"


# DLSETUP             : '$setup';
# DLSETUPHOLD         : '$setuphold';
# DLSKEW              : '$skew';
# DLTIMESKEW          : '$timeskew';
# DLWIDTH             : '$width';
# EDGE                : 'edge' -> pushMode(EDGE_MODE);
# ELSE                : 'else';
# END                 : 'end';
# ENDCASE             : 'endcase';
# ENDCONFIG           : 'endconfig';
# ENDFUNCTION         : 'endfunction';
# ENDGENERATE         : 'endgenerate';
# ENDMODULE           : 'endmodule';
# ENDPRIMITIVE        : 'endprimitive';
# ENDSPECIFY          : 'endspecify';
# ENDTABLE            : 'endtable';
# ENDTASK             : 'endtask';
# EVENT               : 'event';
# FOR                 : 'for';
# FORCE               : 'force';
# FOREVER             : 'forever';
# FORK                : 'fork';
# FUNCTION            : 'function';
# GENERATE            : 'generate';
# GENVAR              : 'genvar';
# HIGHZONE            : 'highz1';
# HIGHZZERO           : 'highz0';
# IF                  : 'if';
# IFNONE              : 'ifnone';
# INCLUDE             : 'include' -> pushMode(LIBRARY_MODE);
# INITIAL             : 'initial';
# INOUT               : 'inout';
# INPUT               : 'input';
# INSTANCE            : 'instance';
# INTEGER             : 'integer';
# JOIN                : 'join';
# LARGE               : 'large';
# LIBLIST             : 'liblist';
# LIBRARY             : 'library' -> pushMode(LIBRARY_MODE);


def gen_DLSETUP(depth=3):
    return "$setup"

def gen_DLSETUPHOLD(depth=3):
    return "$setuphold"

def gen_DLSKEW(depth=3):
    return "$skew"

def gen_DLTIMESKEW(depth=3):
    return "$timeskew"

def gen_DLWIDTH(depth=3):
    return "$width"

def gen_EDGE(depth=3):
    # Pushes EDGE_MODE, reflects the action described in your lexer rule
    return "edge"  # Actual mode switching logic would be context-dependent

def gen_ELSE(depth=3):
    return "else"

def gen_END(depth=3):
    return "end"

def gen_ENDCASE(depth=3):
    return "endcase"

def gen_ENDCONFIG(depth=3):
    return "endconfig"

def gen_ENDFUNCTION(depth=3):
    return "endfunction"

def gen_ENDGENERATE(depth=3):
    return "endgenerate"

def gen_ENDMODULE(depth=3):
    return "endmodule"

def gen_ENDPRIMITIVE(depth=3):
    return "endprimitive"

def gen_ENDSPECIFY(depth=3):
    return "endspecify"

def gen_ENDTABLE(depth=3):
    return "endtable"

def gen_ENDTASK(depth=3):
    return "endtask"

def gen_EVENT(depth=3):
    return "event"

def gen_FOR(depth=3):
    return "for"

def gen_FORCE(depth=3):
    return "force"

def gen_FOREVER(depth=3):
    return "forever"

def gen_FORK(depth=3):
    return "fork"

def gen_FUNCTION(depth=3):
    return "function"

def gen_GENERATE(depth=3):
    return "generate"

def gen_GENVAR(depth=3):
    return "genvar"

def gen_HIGHZONE(depth=3):
    return "highz1"

def gen_HIGHZZERO(depth=3):
    return "highz0"

def gen_IF(depth=3):
    return "if"

def gen_IFNONE(depth=3):
    return "ifnone"

def gen_INCLUDE(depth=3):
    # Pushes LIBRARY_MODE, reflects the action described in your lexer rule
    return "include"  # Actual mode switching logic would be context-dependent

def gen_INITIAL(depth=3):
    return "initial"

def gen_INOUT(depth=3):
    return "inout"

def gen_INPUT(depth=3):
    return "input"

def gen_INSTANCE(depth=3):
    return "instance"

def gen_INTEGER(depth=3):
    return "integer"

def gen_JOIN(depth=3):
    return "join"

def gen_LARGE(depth=3):
    return "large"

def gen_LIBLIST(depth=3):
    return "liblist"

def gen_LIBRARY(depth=3):
    # Pushes LIBRARY_MODE, reflects the action described in your lexer rule
    return "library"  # Actual mode switching logic would be context-dependent



# LOCALPARAM          : 'localparam';
# MACROMODULE         : 'macromodule';
# MEDIUM              : 'medium';
# MIINCDIR            : '-incdir';
# MODULE              : 'module';
# NAND                : 'nand';
# NEGEDGE             : 'negedge';
# NMOS                : 'nmos';
# NOR                 : 'nor';
# NOSHOWCANCELLED     : 'noshowcancelled';
# NOT                 : 'not';
# NOTIFONE            : 'notif1';
# NOTIFZERO           : 'notif0';
# OR                  : 'or';
# OUTPUT              : 'output';
# PARAMETER           : 'parameter';
# PATHPULSEDL         : 'PATHPULSE$';
# PMOS                : 'pmos';
# POSEDGE             : 'posedge';
# PRIMITIVE           : 'primitive';
# PULLDOWN            : 'pulldown';
# PULLONE             : 'pull1';
# PULLUP              : 'pullup';
# PULLZERO            : 'pull0';
# PULSESTYLE_ONDETECT : 'pulsestyle_ondetect';
# PULSESTYLE_ONEVENT  : 'pulsestyle_onevent';
# RCMOS               : 'rcmos';
# REAL                : 'real';
# REALTIME            : 'realtime';
# REG                 : 'reg';
# RELEASE             : 'release';
# REPEAT              : 'repeat';
# RNMOS               : 'rnmos';
# RPMOS               : 'rpmos';
# RTRAN               : 'rtran';
# RTRANIFONE          : 'rtranif1';
# RTRANIFZERO         : 'rtranif0';
# SCALARED            : 'scalared';
# SHOWCANCELLED       : 'showcancelled';
# SIGNED              : 'signed';
# SMALL               : 'small';
# SPECIFY             : 'specify';
# SPECPARAM           : 'specparam';
# STRONGONE           : 'strong1';
# STRONGZERO          : 'strong0';
# SUPPLYONE           : 'supply1';
# SUPPLYZERO          : 'supply0';
# TABLE               : 'table' -> pushMode(TABLE_MODE);
# TASK                : 'task';
# TIME                : 'time';
# TRAN                : 'tran';

def gen_LOCALPARAM(depth=3):
    return "localparam"

def gen_MACROMODULE(depth=3):
    return "macromodule"

def gen_MEDIUM(depth=3):
    return "medium"

def gen_MIINCDIR(depth=3):
    return "-incdir"

def gen_MODULE(depth=3):
    return "module"

def gen_NAND(depth=3):
    return "nand"

def gen_NEGEDGE(depth=3):
    return "negedge"

def gen_NMOS(depth=3):
    return "nmos"

def gen_NOR(depth=3):
    return "nor"

def gen_NOSHOWCANCELLED(depth=3):
    return "noshowcancelled"

def gen_NOT(depth=3):
    return "not"

def gen_NOTIFONE(depth=3):
    return "notif1"

def gen_NOTIFZERO(depth=3):
    return "notif0"

def gen_OR(depth=3):
    return "or"

def gen_OUTPUT(depth=3):
    return "output"

def gen_PARAMETER(depth=3):
    return "parameter"

def gen_PATHPULSEDL(depth=3):
    return "PATHPULSE$"

def gen_PMOS(depth=3):
    return "pmos"

def gen_POSEDGE(depth=3):
    return "posedge"

def gen_PRIMITIVE(depth=3):
    return "primitive"

def gen_PULLDOWN(depth=3):
    return "pulldown"

def gen_PULLONE(depth=3):
    return "pull1"

def gen_PULLUP(depth=3):
    return "pullup"

def gen_PULLZERO(depth=3):
    return "pull0"

def gen_PULSESTYLE_ONDETECT(depth=3):
    return "pulsestyle_ondetect"

def gen_PULSESTYLE_ONEVENT(depth=3):
    return "pulsestyle_onevent"

def gen_RCMOS(depth=3):
    return "rcmos"

def gen_REAL(depth=3):
    return "real"

def gen_REALTIME(depth=3):
    return "realtime"

def gen_REG(depth=3):
    return "reg"

def gen_RELEASE(depth=3):
    return "release"

def gen_REPEAT(depth=3):
    return "repeat"

def gen_RNMOS(depth=3):
    return "rnmos"

def gen_RPMOS(depth=3):
    return "rpmos"

def gen_RTRAN(depth=3):
    return "rtran"

def gen_RTRANIFONE(depth=3):
    return "rtranif1"

def gen_RTRANIFZERO(depth=3):
    return "rtranif0"

def gen_SCALARED(depth=3):
    return "scalared"

def gen_SHOWCANCELLED(depth=3):
    return "showcancelled"

def gen_SIGNED(depth=3):
    return "signed"

def gen_SMALL(depth=3):
    return "small"

def gen_SPECIFY(depth=3):
    return "specify"

def gen_SPECPARAM(depth=3):
    return "specparam"

def gen_STRONGONE(depth=3):
    return "strong1"

def gen_STRONGZERO(depth=3):
    return "strong0"

def gen_SUPPLYONE(depth=3):
    return "supply1"

def gen_SUPPLYZERO(depth=3):
    return "supply0"

def gen_TABLE(depth=3):
    # Pushes TABLE_MODE, reflects the action described in your lexer rule
    return "table"  # Actual mode-switching logic should be handled contextually

def gen_TASK(depth=3):
    return "task"

def gen_TIME(depth=3):
    return "time"

def gen_TRAN(depth=3):
    return "tran"


# TRANIFONE           : 'tranif1';
# TRANIFZERO          : 'tranif0';
# TRI                 : 'tri';
# TRIAND              : 'triand';
# TRIONE              : 'tri1';
# TRIOR               : 'trior';
# TRIREG              : 'trireg';
# TRIZERO             : 'tri0';
# USE                 : 'use';
# UWIRE               : 'uwire';
# VECTORED            : 'vectored';
# WAIT                : 'wait';
# WAND                : 'wand';
# WEAKONE             : 'weak1';
# WEAKZERO            : 'weak0';
# WHILE               : 'while';
# WIRE                : 'wire';
# WOR                 : 'wor';
# XNOR                : 'xnor';
# XOR                 : 'xor';


def gen_TRANIFONE(depth=3):
    return "tranif1"

def gen_TRANIFZERO(depth=3):
    return "tranif0"

def gen_TRI(depth=3):
    return "tri"

def gen_TRIAND(depth=3):
    return "triand"

def gen_TRIONE(depth=3):
    return "tri1"

def gen_TRIOR(depth=3):
    return "trior"

def gen_TRIREG(depth=3):
    return "trireg"

def gen_TRIZERO(depth=3):
    return "tri0"

def gen_USE(depth=3):
    return "use"

def gen_UWIRE(depth=3):
    return "uwire"

def gen_VECTORED(depth=3):
    return "vectored"

def gen_WAIT(depth=3):
    return "wait"

def gen_WAND(depth=3):
    return "wand"

def gen_WEAKONE(depth=3):
    return "weak1"

def gen_WEAKZERO(depth=3):
    return "weak0"

def gen_WHILE(depth=3):
    return "while"

def gen_WIRE(depth=3):
    return "wire"

def gen_WOR(depth=3):
    return "wor"

def gen_XNOR(depth=3):
    return "xnor"

def gen_XOR(depth=3):
    return "xor"


# AM     : '&';
# AMAM   : '&&';
# AMAMAM : '&&&';
# AS     : '*';
# ASAS   : '**';
# ASGT   : '*>';
# AT     : '@';
# CA     : '^';
# CATI   : '^~';
# CL     : ':';
# CO     : ',';
# DL     : '$';
# DQ     : '"';
# DT     : '.';
# EM     : '!';
# EMEQ   : '!=';
# EMEQEQ : '!==';
# EQ     : '=';
# EQEQ   : '==';
# EQEQEQ : '===';
# EQGT   : '=>';
# GA     : '`' -> channel(DIRECTIVES), pushMode(DIRECTIVE_MODE);
# GT     : '>';
# GTEQ   : '>=';
# GTGT   : '>>';
# GTGTGT : '>>>';
# HA     : '#';
# LB     : '[';

def gen_LB(depth=3):
    return "[";

# LC     : '{';

def gen_LC(depth=3):
    return "{";


def gen_AM(depth=3):
    return "&"

def gen_AMAM(depth=3):
    return "&&"

def gen_AMAMAM(depth=3):
    return "&&&"

def gen_AS(depth=3):
    return "*"

def gen_ASAS(depth=3):
    return "**"

def gen_ASGT(depth=3):
    return "*>"

def gen_AT(depth=3):
    return "@"

def gen_CA(depth=3):
    return "^"

def gen_CATI(depth=3):
    return "^~"

def gen_CL(depth=3):
    return ":"

def gen_CO(depth=3):
    return ","

def gen_DL(depth=3):
    return "$"

def gen_DQ(depth=3):
    return '"'

def gen_DT(depth=3):
    return "."

def gen_EM(depth=3):
    return "!"

def gen_EMEQ(depth=3):
    return "!="

def gen_EMEQEQ(depth=3):
    return "!=="

def gen_EQ(depth=3):
    return "="

def gen_EQEQ(depth=3):
    return "=="

def gen_EQEQEQ(depth=3):
    return "==="

def gen_EQGT(depth=3):
    return "=>"

def gen_GA(depth=3):
    # Pushes DIRECTIVES channel and DIRECTIVE_MODE, reflects the lexer rule
    return "`"  # Mode-switching logic should be handled externally

def gen_GT(depth=3):
    return ">"

def gen_GTEQ(depth=3):
    return ">="

def gen_GTGT(depth=3):
    return ">>"

def gen_GTGTGT(depth=3):
    return ">>>"

def gen_HA(depth=3):
    return "#"




#     LP     : '(';
# LT     : '<';
# LTEQ   : '<=';
# LTLT   : '<<';
# LTLTLT : '<<<';
# MI     : '-';
# MICL   : '-:';
# MIGT   : '->';
# MO     : '%';
# PL     : '+';
# PLCL   : '+:';
# QM     : '?';
# RB     : ']';
# RC     : '}';
# RP     : ')';
# SC     : ';';
# SL     : '/';
# TI     : '~';
# TIAM   : '~&';
# TICA   : '~^';
# TIVL   : '~|';
# VL     : '|';
# VLVL   : '||';


def gen_LP(depth=3):
    return "("

def gen_LT(depth=3):
    return "<"

def gen_LTEQ(depth=3):
    return "<="

def gen_LTLT(depth=3):
    return "<<"

def gen_LTLTLT(depth=3):
    return "<<<"

def gen_MI(depth=3):
    return "-"

def gen_MICL(depth=3):
    return "-:"

def gen_MIGT(depth=3):
    return "->"

def gen_MO(depth=3):
    return "%"

def gen_PL(depth=3):
    return "+"

def gen_PLCL(depth=3):
    return "+:"

def gen_QM(depth=3):
    return "?"

def gen_RB(depth=3):
    return "]"

def gen_RC(depth=3):
    return "}"

def gen_RP(depth=3):
    return ")"

def gen_SC(depth=3):
    return ";"

def gen_SL(depth=3):
    return "/"

def gen_TI(depth=3):
    return "~"

def gen_TIAM(depth=3):
    return "~&"

def gen_TICA(depth=3):
    return "~^"

def gen_TIVL(depth=3):
    return "~|"

def gen_VL(depth=3):
    return "|"

def gen_VLVL(depth=3):
    return "||"



# BINARY_BASE          : '\'' [sS]? [bB]       -> pushMode(BINARY_NUMBER_MODE);
# BLOCK_COMMENT        : '/*' ASCII_ANY*? '*/' -> channel(COMMENTS);
# DECIMAL_BASE         : '\'' [sS]? [dD]       -> pushMode(DECIMAL_NUMBER_MODE);
# ESCAPED_IDENTIFIER   : '\\' ASCII_PRINTABLE_NO_SPACE* [ \t\r\n];
# EXPONENTIAL_NUMBER   : UNSIGNED_NUMBER ( '.' UNSIGNED_NUMBER)? [eE] [+\-]? UNSIGNED_NUMBER;
# FIXED_POINT_NUMBER   : UNSIGNED_NUMBER '.' UNSIGNED_NUMBER;
# HEX_BASE             : '\'' [sS]? [hH]        -> pushMode(HEX_NUMBER_MODE);
# LINE_COMMENT         : '//' ASCII_NO_NEWLINE* -> channel(COMMENTS);
# OCTAL_BASE           : '\'' [sS]? [oO]        -> pushMode(OCTAL_NUMBER_MODE);
# SIMPLE_IDENTIFIER    : [a-zA-Z_] [a-zA-Z0-9_$]*;





def gen_BINARY_BASE(depth=3):
    # Pushes BINARY_NUMBER_MODE, reflects the action described in your lexer rule
    return "'b"  # Adjust logic for [sS]? [bB] if needed

def gen_BLOCK_COMMENT(depth=3):
    # Generates a block comment with random content
    return "/* This is a block comment */"

def gen_DECIMAL_BASE(depth=3):
    # Pushes DECIMAL_NUMBER_MODE, reflects the action described in your lexer rule
    return "'d"  # Adjust logic for [sS]? [dD] if needed

def gen_ESCAPED_IDENTIFIER(depth=3):
    # Generates an escaped identifier
    return "\\" + gen_ASCII_PRINTABLE_NO_SPACE(depth-1)
    

def gen_EXPONENTIAL_NUMBER(depth=3):
    # Generates an exponential number
    base = gen_unsigned_number(depth-1)
    fractional = f".{gen_unsigned_number(depth-1)}" if random.choice([True, False]) else ""
    exponent = f"e{random.choice(['+', '-'])}{gen_unsigned_number(depth-1)}"
    return f"{base}{fractional}{exponent}"

def gen_FIXED_POINT_NUMBER(depth=3):
    # Generates a fixed point number
    return f"{gen_unsigned_number(depth-1)}.{gen_unsigned_number(depth-1)}"

def gen_HEX_BASE(depth=3):
    # Pushes HEX_NUMBER_MODE, reflects the action described in your lexer rule
    return "'h"  # Adjust logic for [sS]? [hH] if needed

def gen_LINE_COMMENT(depth=3):
    # Generates a line comment with random content
    return "// This is a line comment"

def gen_OCTAL_BASE(depth=3):
    # Pushes OCTAL_NUMBER_MODE, reflects the action described in your lexer rule
    return "'o"  # Adjust logic for [sS]? [oO] if needed

def gen_SIMPLE_IDENTIFIER(depth=3):
    # Generates a simple identifier
    first_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")
    remaining_chars = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$", k=random.randint(0, 10)))
    return first_char + remaining_chars

# STRING               : '"' ( ASCII_NO_NEWLINE_QUOTE_BACKSLASH | ESC_SPECIAL_CHAR)* '"';
# SYSTEM_TF_IDENTIFIER : '$' [a-zA-Z0-9_$] [a-zA-Z0-9_$]*;

import random
import string

def gen_SYSTEM_TF_IDENTIFIER(depth=3):
    """生成符合 SYSTEM_TF_IDENTIFIER 规则的字符串"""
    length = random.randint(1, 10)  # 生成标识符长度（至少1个字符）
    chars = string.ascii_letters + string.digits + "_$"
    identifier = ''.join(random.choices(chars, k=length))
    return "$" + identifier




def gen_STRING(depth=3):
    """生成符合 STRING 规则的字符串"""
    content = "".join(gen_ASCII_NO_NEWLINE_QUOTE_BACKSLASH(depth-1) if random.random() > 0.3 else gen_ESC_SPECIAL_CHAR(depth-1) for _ in range(random.randint(1, 10)))
    return f'"{content}"'



# UNSIGNED_NUMBER      : [0-9] [0-9_]*;
# WHITE_SPACE          : [ \t\r\n]+ -> channel(HIDDEN);

import random

def gen_UNSIGNED_NUMBER(depth=3):
    """生成符合 UNSIGNED_NUMBER 规则的字符串"""
    num = str(random.randint(0, 9))  # 生成第一位数字（0-9）
    if random.random() > 0.3:  # 以一定概率添加更多数字或下划线
        num += "".join(random.choices("0123456789_", k=random.randint(0, 5)))
    return num.replace("__", "_")  # 避免连续下划线

def gen_WHITE_SPACE(depth=3):
    """生成符合 WHITE_SPACE 规则的字符串"""
    return "".join(random.choices(" \t\r\n", k=random.randint(1, 5)))  # 生成 1-5 个空白字符



# mode BINARY_NUMBER_MODE;
# BINARY_VALUE  : [01xXzZ?] [01xXzZ?_]* -> popMode;
# WHITE_SPACE_0 : WHITE_SPACE           -> channel(HIDDEN), type(WHITE_SPACE);

# mode DECIMAL_NUMBER_MODE;
# UNSIGNED_NUMBER_0 : UNSIGNED_NUMBER -> type(UNSIGNED_NUMBER), popMode;
# WHITE_SPACE_1     : WHITE_SPACE     -> channel(HIDDEN), type(WHITE_SPACE);
# X_OR_Z_UNDERSCORE : [xXzZ?] '_'*    -> popMode;



# For BINARY_NUMBER_MODE
def gen_BINARY_VALUE(depth=3):
    # Generates a binary value
    return "".join(random.choices("01xXzZ?", k=random.randint(1, 5)))

# For DECIMAL_NUMBER_MODE
def gen_UNSIGNED_NUMBER_0(depth=3):
    # Generates an unsigned number in DECIMAL_NUMBER_MODE
    return gen_unsigned_number(depth-1)

def gen_X_OR_Z_UNDERSCORE(depth=3):
    # Generates a value with x/z and underscores
    value = random.choice("xXzZ?")
    underscores = "_" * random.randint(0, 3)
    return f"{value}{underscores}"


# mode EDGE_MODE;
# BLOCK_COMMENT_0 : BLOCK_COMMENT -> channel(COMMENTS), type(BLOCK_COMMENT);
# CO_0            : CO            -> type(CO);
# EDGE_DESCRIPTOR : '01' | '10' | [xXzZ] [01] | [01] [xXzZ];
# GA_0            : GA           -> channel(DIRECTIVES), type(GA), pushMode(DIRECTIVE_MODE);
# LB_0            : LB           -> type(LB);
# LINE_COMMENT_0  : LINE_COMMENT -> channel(COMMENTS), type(LINE_COMMENT);
# RB_0            : RB           -> type(RB), popMode;
# WHITE_SPACE_2   : WHITE_SPACE  -> channel(HIDDEN), type(WHITE_SPACE);

# mode HEX_NUMBER_MODE;
# HEX_VALUE     : [0-9a-fA-FxXzZ?] [0-9a-fA-FxXzZ?_]* -> popMode;
# WHITE_SPACE_3 : WHITE_SPACE                         -> channel(HIDDEN), type(WHITE_SPACE);

# mode LIBRARY_MODE;
# BLOCK_COMMENT_1      : BLOCK_COMMENT      -> channel(COMMENTS), type(BLOCK_COMMENT);
# CO_1                 : CO                 -> type(CO);
# ESCAPED_IDENTIFIER_0 : ESCAPED_IDENTIFIER -> type(ESCAPED_IDENTIFIER);
# GA_1                 : GA                 -> channel(DIRECTIVES), type(GA), pushMode(DIRECTIVE_MODE);
# LINE_COMMENT_1       : LINE_COMMENT       -> channel(COMMENTS), type(LINE_COMMENT);
# MIINCDIR_0           : MIINCDIR           -> type(MIINCDIR);
# SC_0                 : SC                 -> type(SC), popMode;



def gen_BLOCK_COMMENT_0(depth=3):
    # Generates a block comment, matching the BLOCK_COMMENT rule
    return "/* This is a block comment */"

def gen_CO_0(depth=3):
    # Generates a comma, type(CO)
    return ","

def gen_EDGE_DESCRIPTOR(depth=3):
    # Generates an edge descriptor
    return random.choice(["01", "10", f"{random.choice('xXzZ')}{random.choice('01')}", f"{random.choice('01')}{random.choice('xXzZ')}"])

def gen_GA_0(depth=3):
    # Handles GA rule, pushes DIRECTIVE_MODE
    return "`"  # Contextual mode handling required externally

def gen_LB_0(depth=3):
    # Generates a left bracket, type(LB)
    return "["

def gen_LINE_COMMENT_0(depth=3):
    # Generates a line comment, matching LINE_COMMENT
    return "// This is a line comment"

def gen_RB_0(depth=3):
    # Generates a right bracket and indicates popMode
    return "]"

def gen_WHITE_SPACE_2(depth=3):
    # Generates white space
    return " " * random.randint(1, 5)


def gen_HEX_VALUE(depth=3):
    # Generates a hexadecimal value
    return "".join(random.choices("0123456789abcdefABCDEFxXzZ?", k=random.randint(1, 10)))

def gen_WHITE_SPACE_3(depth=3):
    # Generates white space
    return " " * random.randint(1, 5)


def gen_BLOCK_COMMENT_1(depth=3):
    # Generates a block comment for LIBRARY_MODE
    return "/* Library-specific block comment */"

def gen_CO_1(depth=3):
    # Generates a comma, type(CO)
    return ","

def gen_ESCAPED_IDENTIFIER_0(depth=3):
    # Generates an escaped identifier
    return "\\" + gen_ASCII_PRINTABLE_NO_SPACE(depth-1)

def gen_GA_1(depth=3):
    # Handles GA rule in LIBRARY_MODE, pushes DIRECTIVE_MODE
    return "`"  # Contextual mode handling required externally

def gen_LINE_COMMENT_1(depth=3):
    # Generates a line comment for LIBRARY_MODE
    return "// Library-specific line comment"

def gen_MIINCDIR_0(depth=3):
    # Generates the '-incdir' token
    return "-incdir"

def gen_SC_0(depth=3):
    # Generates a semicolon and indicates popMode
    return ";"

# SIMPLE_IDENTIFIER_0  : SIMPLE_IDENTIFIER  -> type(SIMPLE_IDENTIFIER);
# WHITE_SPACE_4        : WHITE_SPACE        -> channel(HIDDEN), type(WHITE_SPACE);
# FILE_PATH_SPEC       : ( [a-zA-Z0-9_./] | ESC_ASCII_PRINTABLE)+ | STRING;

import random
import string

def gen_SIMPLE_IDENTIFIER_0(depth=3):
    """生成符合 SIMPLE_IDENTIFIER_0 规则的字符串"""
    return gen_SIMPLE_IDENTIFIER(depth-1)  # 直接调用 SIMPLE_IDENTIFIER 生成函数

def gen_WHITE_SPACE_4(depth=3):
    """生成符合 WHITE_SPACE_4 规则的字符串"""
    return gen_WHITE_SPACE(depth-1)  # 直接调用 WHITE_SPACE 生成函数

def gen_FILE_PATH_SPEC(depth=3):
    """生成符合 FILE_PATH_SPEC 规则的字符串"""
    if random.random() > 0.5:
        length = random.randint(5, 15)
        chars = string.ascii_letters + string.digits + "_./"
        return "".join(random.choices(chars, k=length))  # 生成随机文件路径字符
    else:
        return gen_STRING(depth-1)  # 直接调用 STRING 生成函数


# mode OCTAL_NUMBER_MODE;
# OCTAL_VALUE   : [0-7xXzZ?] [0-7xXzZ?_]* -> popMode;
# WHITE_SPACE_5 : WHITE_SPACE             -> channel(HIDDEN), type(WHITE_SPACE);

def gen_OCTAL_VALUE(depth=3):
    # Generates an octal value
    return "".join(random.choices("01234567xXzZ?", k=random.randint(1, 10)))

def gen_WHITE_SPACE_5(depth=3):
    # Generates white space
    return " " * random.randint(1, 5)


# mode TABLE_MODE;
# BLOCK_COMMENT_2        : BLOCK_COMMENT -> channel(COMMENTS), type(BLOCK_COMMENT);
# CL_0                   : CL            -> type(CL);
# EDGE_SYMBOL            : [rRfFpPnN*];
# ENDTABLE_0             : ENDTABLE -> type(ENDTABLE), popMode;
# GA_2                   : GA       -> channel(DIRECTIVES), type(GA), pushMode(DIRECTIVE_MODE);
# LEVEL_ONLY_SYMBOL      : [?bB];
# LINE_COMMENT_2         : LINE_COMMENT -> channel(COMMENTS), type(LINE_COMMENT);
# LP_0                   : LP           -> type(LP);
# MI_0                   : MI           -> type(MI);
# OUTPUT_OR_LEVEL_SYMBOL : [01xX];
# RP_0                   : RP          -> type(RP);
# SC_1                   : SC          -> type(SC);
# WHITE_SPACE_6          : WHITE_SPACE -> channel(HIDDEN), type(WHITE_SPACE);

# mode DIRECTIVE_MODE;
# BEGIN_KEYWORDS_DIRECTIVE:
#     'begin_keywords' -> channel(DIRECTIVES), mode(BEGIN_KEYWORDS_DIRECTIVE_MODE)
# ;
# CELLDEFINE_DIRECTIVE: 'celldefine' -> channel(DIRECTIVES), popMode;
# DEFAULT_NETTYPE_DIRECTIVE:
#     'default_nettype' -> channel(DIRECTIVES), mode(DEFAULT_NETTYPE_DIRECTIVE_MODE)
# ;


def gen_BLOCK_COMMENT_2(depth=3):
    # Generates a block comment
    return "/* Table-specific block comment */"

def gen_CL_0(depth=3):
    # Generates a colon, type(CL)
    return ":"

def gen_EDGE_SYMBOL(depth=3):
    # Generates an edge symbol
    return random.choice("rRfFpPnN*")

def gen_ENDTABLE_0(depth=3):
    # Generates "endtable" and indicates popMode
    return "endtable"

def gen_GA_2(depth=3):
    # Handles GA, pushing DIRECTIVE_MODE
    return "`"  # Contextual mode switching handled externally

def gen_LEVEL_ONLY_SYMBOL(depth=3):
    # Generates a level-only symbol
    return random.choice("?bB")

def gen_LINE_COMMENT_2(depth=3):
    # Generates a line comment for TABLE_MODE
    return "// Table-specific line comment"

def gen_LP_0(depth=3):
    # Generates a left parenthesis, type(LP)
    return "("

def gen_MI_0(depth=3):
    # Generates a minus sign, type(MI)
    return "-"

def gen_OUTPUT_OR_LEVEL_SYMBOL(depth=3):
    # Generates an output or level symbol
    return random.choice("01xX")

def gen_RP_0(depth=3):
    # Generates a right parenthesis, type(RP)
    return ")"

def gen_SC_1(depth=3):
    # Generates a semicolon, type(SC)
    return ";"

def gen_WHITE_SPACE_6(depth=3):
    # Generates white space
    return " " * random.randint(1, 5)


def gen_BEGIN_KEYWORDS_DIRECTIVE(depth=3):
    # Generates "begin_keywords" and switches to BEGIN_KEYWORDS_DIRECTIVE_MODE
    return "begin_keywords"  # Mode switch context handled externally

def gen_CELLDEFINE_DIRECTIVE(depth=3):
    # Generates "celldefine" and indicates popMode
    return "celldefine"

def gen_DEFAULT_NETTYPE_DIRECTIVE(depth=3):
    # Generates "default_nettype" and switches to DEFAULT_NETTYPE_DIRECTIVE_MODE
    return "default_nettype"  # Mode switch context handled externally

# DEFINE_DIRECTIVE              : 'define'              -> channel(DIRECTIVES), mode(DEFINE_DIRECTIVE_MODE);
# ELSE_DIRECTIVE                : 'else'                -> channel(DIRECTIVES), popMode, mode(ELSE_DIRECTIVE_MODE);
# ELSIF_DIRECTIVE               : 'elsif'               -> channel(DIRECTIVES), popMode, mode(ELSIF_DIRECTIVE_MODE);
# END_KEYWORDS_DIRECTIVE        : 'end_keywords'        -> channel(DIRECTIVES), popMode;
# ENDCELLDEFINE_DIRECTIVE       : 'endcelldefine'       -> channel(DIRECTIVES), popMode;
# ENDIF_DIRECTIVE               : 'endif'               -> channel(DIRECTIVES), popMode, popMode, popMode;
# IFDEF_DIRECTIVE               : 'ifdef'               -> channel(DIRECTIVES), mode(IFDEF_DIRECTIVE_MODE);
# IFNDEF_DIRECTIVE              : 'ifndef'              -> channel(DIRECTIVES), mode(IFDEF_DIRECTIVE_MODE);
# INCLUDE_DIRECTIVE             : 'include'             -> channel(DIRECTIVES), mode(INCLUDE_DIRECTIVE_MODE);
# LINE_DIRECTIVE                : 'line'                -> channel(DIRECTIVES), mode(LINE_DIRECTIVE_MODE);
# NOUNCONNECTED_DRIVE_DIRECTIVE : 'nounconnected_drive' -> channel(DIRECTIVES), popMode;
# PRAGMA_DIRECTIVE              : 'pragma'              -> channel(DIRECTIVES), mode(PRAGMA_DIRECTIVE_MODE);
# RESETALL_DIRECTIVE            : 'resetall'            -> channel(DIRECTIVES), popMode;
# TIMESCALE_DIRECTIVE           : 'timescale'           -> channel(DIRECTIVES), mode(TIMESCALE_DIRECTIVE_MODE);
# UNCONNECTED_DRIVE_DIRECTIVE:
#     'unconnected_drive' -> channel(DIRECTIVES), mode(UNCONNECTED_DRIVE_DIRECTIVE_MODE)
# ;
# UNDEF_DIRECTIVE : 'undef'                                -> channel(DIRECTIVES), mode(UNDEF_DIRECTIVE_MODE);



def gen_DEFINE_DIRECTIVE(depth=3):
    # Generates "define" and switches to DEFINE_DIRECTIVE_MODE
    return "define"

def gen_ELSE_DIRECTIVE(depth=3):
    # Generates "else", pops the current mode, and switches to ELSE_DIRECTIVE_MODE
    return "else"

def gen_ELSIF_DIRECTIVE(depth=3):
    # Generates "elsif", pops the current mode, and switches to ELSIF_DIRECTIVE_MODE
    return "elsif"

def gen_END_KEYWORDS_DIRECTIVE(depth=3):
    # Generates "end_keywords" and pops the current mode
    return "end_keywords"

def gen_ENDCELLDEFINE_DIRECTIVE(depth=3):
    # Generates "endcelldefine" and pops the current mode
    return "endcelldefine"

def gen_ENDIF_DIRECTIVE(depth=3):
    # Generates "endif" and pops three modes
    return "endif"

def gen_IFDEF_DIRECTIVE(depth=3):
    # Generates "ifdef" and switches to IFDEF_DIRECTIVE_MODE
    return "ifdef"

def gen_IFNDEF_DIRECTIVE(depth=3):
    # Generates "ifndef" and switches to IFDEF_DIRECTIVE_MODE
    return "ifndef"

def gen_INCLUDE_DIRECTIVE(depth=3):
    # Generates "include" and switches to INCLUDE_DIRECTIVE_MODE
    return "include"

def gen_LINE_DIRECTIVE(depth=3):
    # Generates "line" and switches to LINE_DIRECTIVE_MODE
    return "line"

def gen_NOUNCONNECTED_DRIVE_DIRECTIVE(depth=3):
    # Generates "nounconnected_drive" and pops the current mode
    return "nounconnected_drive"

def gen_PRAGMA_DIRECTIVE(depth=3):
    # Generates "pragma" and switches to PRAGMA_DIRECTIVE_MODE
    return "pragma"

def gen_RESETALL_DIRECTIVE(depth=3):
    # Generates "resetall" and pops the current mode
    return "resetall"

def gen_TIMESCALE_DIRECTIVE(depth=3):
    # Generates "timescale" and switches to TIMESCALE_DIRECTIVE_MODE
    return "timescale"

def gen_UNCONNECTED_DRIVE_DIRECTIVE(depth=3):
    # Generates "unconnected_drive" and switches to UNCONNECTED_DRIVE_DIRECTIVE_MODE
    return "unconnected_drive"

def gen_UNDEF_DIRECTIVE(depth=3):
    # Generates "undef" and switches to UNDEF_DIRECTIVE_MODE
    return "undef"


# MACRO_USAGE     : IDENTIFIER ( WHITE_SPACE? MACRO_ARGS)? -> channel(DIRECTIVES), popMode;

import random

def gen_MACRO_USAGE(depth=3):
    """
    生成符合 MACRO_USAGE 产生式的字符串：
        MACRO_USAGE : IDENTIFIER ( WHITE_SPACE? MACRO_ARGS )? -> channel(DIRECTIVES), popMode

    说明：
      - 先生成 IDENTIFIER，
      - 可选部分是：( WHITE_SPACE? MACRO_ARGS )，其中 WHITE_SPACE 是可选的，
        根据实际情况随机选择是否生成（可视需求调整策略）。
      - "-> channel(DIRECTIVES), popMode" 为 lexer 的动作，这里不生成到返回字符串中。
    """
    # 生成 IDENTIFIER 部分
    result = gen_IDENTIFIER(depth-1)
    
    # 随机决定是否生成可选组 ( WHITE_SPACE? MACRO_ARGS )
    if random.choice([True, False]):
        # 可选的 WHITE_SPACE 部分：随机生成一个或者不生成
        if random.choice([True, False]):
            result += gen_WHITE_SPACE(depth-1)
        # 生成 MACRO_ARGS 部分
        result += gen_MACRO_ARGS(depth-1)
    
    return result



# mode BEGIN_KEYWORDS_DIRECTIVE_MODE;
# BLOCK_COMMENT_3 : BLOCK_COMMENT -> channel(COMMENTS), type(BLOCK_COMMENT);
# DQ_0            : DQ            -> channel(DIRECTIVES), type(DQ);
# NEWLINE_0       : NEWLINE       -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_0     : SPACE_TAB     -> channel(HIDDEN), type(WHITE_SPACE);
# VERSION_SPECIFIER:
#     ('1364-2005' | '1364-2001' | '1364-2001-noconfig' | '1364-1995') -> channel(DIRECTIVES)
# ;

def gen_BLOCK_COMMENT_3(depth=3):
    # Generates a block comment
    return "/* Begin-keywords-specific block comment */"

def gen_DQ_0(depth=3):
    # Generates a double quote, channel is set to DIRECTIVES
    return '"'

def gen_NEWLINE_0(depth=3):
    # Generates a newline and pops the current mode
    return "\n"

def gen_SPACE_TAB_0(depth=3):
    # Generates space or tab for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_VERSION_SPECIFIER(depth=3):
    # Generates a version specifier
    return random.choice(["1364-2005", "1364-2001", "1364-2001-noconfig", "1364-1995"])


# mode DEFAULT_NETTYPE_DIRECTIVE_MODE;
# BLOCK_COMMENT_4: BLOCK_COMMENT -> channel(COMMENTS), type(BLOCK_COMMENT);
# DEFAULT_NETTYPE_VALUE:
#     (
#         'wire'
#         | 'tri'
#         | 'tri0'
#         | 'tri1'
#         | 'wand'
#         | 'triand'
#         | 'wor'
#         | 'trior'
#         | 'trireg'
#         | 'uwire'
#         | 'none'
#     ) -> channel(DIRECTIVES), popMode
# ;
# NEWLINE_1   : NEWLINE   -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_1 : SPACE_TAB -> channel(HIDDEN), type(WHITE_SPACE);



def gen_BLOCK_COMMENT_4(depth=3):
    # Generates a block comment
    return "/* Default-nettype-specific block comment */"

def gen_DEFAULT_NETTYPE_VALUE(depth=3):
    # Generates one of the default nettype values and pops the mode
    return random.choice(["wire", "tri", "tri0", "tri1", "wand", "triand", "wor", "trior", "trireg", "uwire", "none"])

def gen_NEWLINE_1(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_1(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)



# mode DEFINE_DIRECTIVE_MODE;
# MACRO_NAME   : IDENTIFIER MACRO_ARGS? -> channel(DIRECTIVES), mode(MACRO_TEXT_MODE);

import random

def gen_MACRO_NAME(depth=3):
    """
    生成符合 MACRO_NAME 产生式的字符串：
       MACRO_NAME : IDENTIFIER MACRO_ARGS? -> channel(DIRECTIVES), mode(MACRO_TEXT_MODE)
       
    说明：
      - 首先生成 IDENTIFIER 部分；
      - 然后随机决定是否生成可选部分 MACRO_ARGS；
      - 最后的动作部分不影响生成的字符串。
    """
    result = gen_IDENTIFIER(depth-1)
    
    # MACRO_ARGS 为可选项，随机决定是否生成
    if random.choice([True, False]):
        result += gen_MACRO_ARGS(depth-1)
    
    return result



# NEWLINE_12   : NEWLINE                -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_11 : SPACE_TAB              -> channel(HIDDEN), type(WHITE_SPACE);

# mode ELSE_DIRECTIVE_MODE;
# NEWLINE_8   : NEWLINE   -> channel(HIDDEN), type(WHITE_SPACE), mode(SOURCE_TEXT_MODE);
# SPACE_TAB_7 : SPACE_TAB -> channel(HIDDEN), type(WHITE_SPACE);

# mode ELSIF_DIRECTIVE_MODE;
# IDENTIFIER_0 : IDENTIFIER -> channel(DIRECTIVES), type(MACRO_IDENTIFIER);
# NEWLINE_9    : NEWLINE    -> channel(HIDDEN), type(WHITE_SPACE), mode(SOURCE_TEXT_MODE);
# SPACE_TAB_8  : SPACE_TAB  -> channel(HIDDEN), type(WHITE_SPACE);



def gen_NEWLINE_12(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_11(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)


def gen_NEWLINE_8(depth=3):
    # Generates a newline and switches to SOURCE_TEXT_MODE
    return "\n"

def gen_SPACE_TAB_7(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_IDENTIFIER_0(depth=3):
    # Generates an identifier and sets type as MACRO_IDENTIFIER
    return gen_identifier(depth-1)

def gen_NEWLINE_9(depth=3):
    # Generates a newline and switches to SOURCE_TEXT_MODE
    return "\n"

def gen_SPACE_TAB_8(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)



# mode FILENAME_MODE;
# DQ_1     : DQ                                                           -> channel(DIRECTIVES), type(DQ), popMode;
# FILENAME : ( ASCII_PRINTABLE_NO_QUOTE_BACKSLASH | ESC_ASCII_PRINTABLE)+ -> channel(DIRECTIVES);

# mode IFDEF_DIRECTIVE_MODE;
# IDENTIFIER_1 : IDENTIFIER -> channel(DIRECTIVES), type(MACRO_IDENTIFIER);
# NEWLINE_10   : NEWLINE    -> channel(HIDDEN), type(WHITE_SPACE), pushMode(SOURCE_TEXT_MODE);
# SPACE_TAB_9  : SPACE_TAB  -> channel(HIDDEN), type(WHITE_SPACE);

# mode INCLUDE_DIRECTIVE_MODE;
# DQ_2        : DQ        -> channel(DIRECTIVES), type(DQ), pushMode(FILENAME_MODE);
# NEWLINE_2   : NEWLINE   -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_2 : SPACE_TAB -> channel(HIDDEN), type(WHITE_SPACE);

# mode LINE_DIRECTIVE_MODE;
# DQ_3              : DQ              -> channel(DIRECTIVES), type(DQ), pushMode(FILENAME_MODE);
# NEWLINE_3         : NEWLINE         -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_3       : SPACE_TAB       -> channel(HIDDEN), type(WHITE_SPACE);
# UNSIGNED_NUMBER_1 : UNSIGNED_NUMBER -> channel(DIRECTIVES), type(UNSIGNED_NUMBER);


def gen_DQ_1(depth=3):
    # Generates a double quote, sets channel to DIRECTIVES, and pops the mode
    return '"'

def gen_FILENAME(depth=3):
    # Generates a filename using allowed characters
    return "/path/to/file"  # Adjust logic if needed to include ASCII_PRINTABLE_NO_QUOTE_BACKSLASH or ESC_ASCII_PRINTABLE


def gen_IDENTIFIER_1(depth=3):
    # Generates an identifier and sets type as MACRO_IDENTIFIER
    return gen_identifier(depth-1)

def gen_NEWLINE_10(depth=3):
    # Generates a newline and switches to SOURCE_TEXT_MODE
    return "\n"

def gen_SPACE_TAB_9(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)


def gen_DQ_2(depth=3):
    # Generates a double quote, sets channel to DIRECTIVES, and switches to FILENAME_MODE
    return '"'

def gen_NEWLINE_2(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_2(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)


def gen_DQ_3(depth=3):
    # Generates a double quote, sets channel to DIRECTIVES, and switches to FILENAME_MODE
    return '"'

def gen_NEWLINE_3(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_3(depth=3):
    # Generates spaces or tabs as whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_UNSIGNED_NUMBER_1(depth=3):
    # Generates an unsigned number and sets type as UNSIGNED_NUMBER
    return gen_unsigned_number(depth-1)  # Assume `gen_unsigned_number` is implemented




# mode MACRO_TEXT_MODE;
# BLOCK_COMMENT_5   : BLOCK_COMMENT                                        -> channel(COMMENTS), type(BLOCK_COMMENT);
# GA_3              : GA                                                   -> channel(DIRECTIVES), type(MACRO_TEXT);
# MACRO_DELIMITER   : '``'                                                 -> channel(DIRECTIVES);
# MACRO_ESC_NEWLINE : ESC_NEWLINE                                          -> channel(DIRECTIVES);
# MACRO_ESC_QUOTE   : '`\\`"'                                              -> channel(DIRECTIVES);




def gen_BLOCK_COMMENT_5(depth=3):
    # Generates a block comment
    return "/* Macro-text-specific block comment */"

def gen_GA_3(depth=3):
    # Generates a backtick character (`), set as MACRO_TEXT
    return "`"

def gen_MACRO_DELIMITER(depth=3):
    # Generates a macro delimiter
    return "``"

def gen_MACRO_ESC_NEWLINE(depth=3):
    # Generates an escaped newline
    return "\\\n"

def gen_MACRO_ESC_QUOTE(depth=3):
    # Generates an escaped quote sequence
    return '`\\"'


# MACRO_ESC_SEQ     : ESC_ASCII_NO_NEWLINE                                 -> channel(DIRECTIVES), type(MACRO_TEXT);

def gen_MACRO_ESC_SEQ(depth=3):
    """
    生成符合 MACRO_ESC_SEQ 产生式的字符串：
        MACRO_ESC_SEQ : ESC_ASCII_NO_NEWLINE -> channel(DIRECTIVES), type(MACRO_TEXT)
    
    说明：
      - 调用 gen_ESC_ASCII_NO_NEWLINE(depth-1) 生成对应部分的字符串。
      - 动作部分不影响返回的字符串。
    """
    return gen_ESC_ASCII_NO_NEWLINE(depth-1)



# MACRO_QUOTE       : '`"'                                                 -> channel(DIRECTIVES);
# MACRO_TEXT        : ASCII_NO_NEWLINE_QUOTE_SLASH_BACKSLASH_GRAVE_ACCENT+ -> channel(DIRECTIVES);
# NEWLINE_4         : NEWLINE                                              -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SL_2              : SL                                                   -> more;



def gen_MACRO_QUOTE(depth=3):
    # Generates a backtick and double quote
    return '`"'

def gen_MACRO_TEXT(depth=3):
    # Generates macro text without disallowed characters
    return "text_without_special_chars"  # Adjust based on ASCII constraints

def gen_NEWLINE_4(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SL_2(depth=3):
    # Generates a slash (`/`), with the `more` flag
    return "/"

# STRING_0          : STRING                                               -> channel(DIRECTIVES), type(STRING);

def gen_STRING_0(depth=3):
    """
    生成符合 STRING_0 产生式的字符串：
      STRING_0 : STRING -> channel(DIRECTIVES), type(STRING)
    
    说明：
      - 调用 gen_STRING(depth-1) 生成对应部分的字符串。
      - lexer 指定的动作部分不参与生成返回的字符串。
    """
    return gen_STRING(depth-1)


# mode PRAGMA_DIRECTIVE_MODE;
# BLOCK_COMMENT_6     : BLOCK_COMMENT     -> channel(COMMENTS), type(BLOCK_COMMENT);
# CO_2                : CO                -> channel(DIRECTIVES), type(CO);
# EQ_0                : EQ                -> channel(DIRECTIVES), type(EQ);
# LP_1                : LP                -> channel(DIRECTIVES), type(LP);
# NEWLINE_5           : NEWLINE           -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# RP_1                : RP                -> channel(DIRECTIVES), type(RP);
# SIMPLE_IDENTIFIER_1 : SIMPLE_IDENTIFIER -> channel(DIRECTIVES), type(SIMPLE_IDENTIFIER);
# SPACE_TAB_4         : SPACE_TAB         -> channel(HIDDEN), type(WHITE_SPACE);




def gen_BLOCK_COMMENT_6(depth=3):
    # Generates a block comment for pragma directives
    return "/* Pragma-specific block comment */"

def gen_CO_2(depth=3):
    # Generates a comma
    return ","

def gen_EQ_0(depth=3):
    # Generates an equals sign
    return "="

def gen_LP_1(depth=3):
    # Generates a left parenthesis
    return "("

def gen_NEWLINE_5(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_RP_1(depth=3):
    # Generates a right parenthesis
    return ")"

def gen_SIMPLE_IDENTIFIER_1(depth=3):
    # Generates a simple identifier
    return gen_simple_identifier(depth-1)  # Assume this function is implemented

def gen_SPACE_TAB_4(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)


# STRING_1            : STRING            -> channel(DIRECTIVES), type(STRING);

def gen_STRING_1(depth=3):
    """
    生成符合 STRING_1 产生式的字符串：
       STRING_1 : STRING -> channel(DIRECTIVES), type(STRING)
    
    说明：
      - 直接调用 gen_STRING(depth-1) 生成 STRING 部分。
      - lexer 动作部分对生成结果没有影响，不参与返回值。
    """
    return gen_STRING(depth-1)



# UNSIGNED_NUMBER_2   : UNSIGNED_NUMBER   -> channel(DIRECTIVES), type(UNSIGNED_NUMBER);

# mode SOURCE_TEXT_MODE;
# BLOCK_COMMENT_7 : BLOCK_COMMENT                -> channel(COMMENTS), type(BLOCK_COMMENT);
# GA_4            : GA                           -> channel(DIRECTIVES), type(GA), pushMode(DIRECTIVE_MODE);
# LINE_COMMENT_3  : LINE_COMMENT                 -> channel(COMMENTS), type(LINE_COMMENT);
# SL_0            : SL                           -> more;
# SOURCE_TEXT     : ASCII_NO_SLASH_GRAVE_ACCENT+ -> channel(DIRECTIVES);

# mode TIMESCALE_DIRECTIVE_MODE;
# BLOCK_COMMENT_8 : BLOCK_COMMENT         -> channel(COMMENTS), type(BLOCK_COMMENT);
# NEWLINE_6       : NEWLINE               -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SL_1            : SL                    -> channel(DIRECTIVES), type(SL);
# SPACE_TAB_5     : SPACE_TAB             -> channel(HIDDEN), type(WHITE_SPACE);
# TIME_UNIT       : [munpf]? 's'          -> channel(DIRECTIVES);
# TIME_VALUE      : ( '1' | '10' | '100') -> channel(DIRECTIVES);


def gen_UNSIGNED_NUMBER_2(depth=3):
    # Generates an unsigned number
    return gen_unsigned_number(depth-1)  # Assume this function is implemented

def gen_BLOCK_COMMENT_6(depth=3):
    # Generates a block comment for pragma directives
    return "/* Pragma-specific block comment */"

def gen_CO_2(depth=3):
    # Generates a comma
    return ","

def gen_EQ_0(depth=3):
    # Generates an equals sign
    return "="

def gen_LP_1(depth=3):
    # Generates a left parenthesis
    return "("

def gen_NEWLINE_5(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_RP_1(depth=3):
    # Generates a right parenthesis
    return ")"

def gen_SIMPLE_IDENTIFIER_1(depth=3):
    # Generates a simple identifier
    return gen_simple_identifier(depth-1)  # Assume this function is implemented

def gen_SPACE_TAB_4(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)


def gen_UNSIGNED_NUMBER_2(depth=3):
    # Generates an unsigned number
    return gen_unsigned_number(depth-1)  # Assume this function is implemented

def gen_BLOCK_COMMENT_7(depth=3):
    # Generates a block comment for source text
    return "/* Source-text-specific block comment */"

def gen_GA_4(depth=3):
    # Generates a backtick character (`), switches to DIRECTIVE_MODE
    return "`"

def gen_LINE_COMMENT_3(depth=3):
    # Generates a line comment
    return "// Source-text-specific line comment"

def gen_SL_0(depth=3):
    # Generates a slash (`/`), with the `more` flag
    return "/"

def gen_SOURCE_TEXT(depth=3):
    # Generates source text without slash or backtick
    return "source_text_without_special_chars"  # Adjust based on ASCII constraints


def gen_BLOCK_COMMENT_8(depth=3):
    # Generates a block comment for timescale directives
    return "/* Timescale-specific block comment */"

def gen_NEWLINE_6(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SL_1(depth=3):
    # Generates a slash (`/`)
    return "/"

def gen_SPACE_TAB_5(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_TIME_UNIT(depth=3):
    # Generates a time unit with optional prefix
    return f"{random.choice(['', 'm', 'u', 'n', 'p', 'f'])}s"

def gen_TIME_VALUE(depth=3):
    # Generates a time value (1, 10, or 100)
    return random.choice(["1", "10", "100"])



# mode UNCONNECTED_DRIVE_DIRECTIVE_MODE;
# BLOCK_COMMENT_9         : BLOCK_COMMENT        -> channel(COMMENTS), type(BLOCK_COMMENT);
# NEWLINE_7               : NEWLINE              -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_6             : SPACE_TAB            -> channel(HIDDEN), type(WHITE_SPACE);
# UNCONNECTED_DRIVE_VALUE : ( 'pull0' | 'pull1') -> channel(DIRECTIVES), popMode;

# mode UNDEF_DIRECTIVE_MODE;
# MACRO_IDENTIFIER : IDENTIFIER -> channel(DIRECTIVES);
# NEWLINE_11       : NEWLINE    -> channel(HIDDEN), type(WHITE_SPACE), popMode;
# SPACE_TAB_10     : SPACE_TAB  -> channel(HIDDEN), type(WHITE_SPACE);

# fragment ASCII_ANY        : [\u0000-\u007f];
# fragment ASCII_NO_NEWLINE : [\u0000-\u0009\u000b-\u000c\u000e-\u007f];
# fragment ASCII_NO_NEWLINE_QUOTE_BACKSLASH:
#     [\u0000-\u0009\u000b-\u000c\u000e-\u0021\u0023-\u005b\u005d-\u007f]
# ;
# fragment ASCII_NO_NEWLINE_QUOTE_SLASH_BACKSLASH_GRAVE_ACCENT:
#     [\u0000-\u0009\u000b-\u000c\u000e-\u0021\u0023-\u002e\u0030-\u005b\u005d-\u005f\u0061-\u007f]
# ;
# fragment ASCII_NO_PARENTHESES               : [\u0000-\u0027\u002a-\u007f];

import random

def gen_ASCII_NO_PARENTHESES(depth=3):
    """
    生成符合 ASCII_NO_PARENTHESES 定义的字符：
      ASCII_NO_PARENTHESES : [\u0000-\u0027\u002a-\u007f]
    
    说明：
      - 该字符的 Unicode 代码点位于两个区间之一：
          区间1: [\u0000, \u0027] （十进制 0 - 39）
          区间2: [\u002a, \u007f] （十进制 42 - 127）
      - 先随机选择一个区间，再从该区间内选取一个随机字符返回。
    """
    if random.choice([True, False]):
        # 选取区间 [\u0000-\u0027]
        code_point = random.randint(0x0000, 0x0027)
    else:
        # 选取区间 [\u002a-\u007f]
        code_point = random.randint(0x002a, 0x007f)
    return chr(code_point)




# fragment ASCII_NO_SLASH_GRAVE_ACCENT        : [\u0000-\u002e\u0030-\u005f\u0061-\u007f];
# fragment ASCII_PRINTABLE                    : [\u0020-\u007e];
# fragment ASCII_PRINTABLE_NO_QUOTE_BACKSLASH : [\u0020-\u0021\u0023-\u005b\u005d-\u007e];
# fragment ASCII_PRINTABLE_NO_SPACE           : [\u0021-\u007e];
# fragment CHAR_OCTAL                         : [0-7] [0-7]? [0-7]?;

import random

def gen_CHAR_OCTAL(depth=3):
    """生成符合 CHAR_OCTAL 规则的字符串"""
    length = random.randint(1, 3)  # 生成 1 到 3 位的八进制数
    return "".join(random.choices("01234567", k=length))


# fragment ESC_ASCII_NO_NEWLINE               : '\\' ASCII_NO_NEWLINE;
# fragment ESC_ASCII_PRINTABLE                : '\\' ASCII_PRINTABLE;
# fragment ESC_NEWLINE                        : '\\' NEWLINE;
# fragment ESC_SPECIAL_CHAR                   : '\\' ( [nt\\"] | CHAR_OCTAL);

import random

def gen_ESC_SPECIAL_CHAR(depth=3):
    """生成符合 ESC_SPECIAL_CHAR 规则的字符串"""
    options = ["\\n", "\\t", "\\\\", "\\\""]
    return random.choice(options) if random.random() > 0.5 else gen_CHAR_OCTAL(depth-1)

# fragment IDENTIFIER                         : ESCAPED_IDENTIFIER | SIMPLE_IDENTIFIER;



def gen_BLOCK_COMMENT_9(depth=3):
    # Generates a block comment
    return "/* Unconnected-drive-specific block comment */"

def gen_NEWLINE_7(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_6(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_UNCONNECTED_DRIVE_VALUE(depth=3):
    # Generates a unconnected drive value (pull0 or pull1) and pops the mode
    return random.choice(["pull0", "pull1"])


def gen_MACRO_IDENTIFIER(depth=3):
    # Generates a macro identifier
    return gen_identifier(depth-1)  # Assumes gen_identifier(depth-1) is implemented

def gen_NEWLINE_11(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_10(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)


def gen_ascii_no_newline(depth=3):
    # Generates ASCII characters without newlines
    return "".join(random.choices("\u0000\u0009\u000b\u000c\u000e-\u007f", k=5))

def gen_ascii_printable(depth=3):
    # Generates printable ASCII characters
    return "".join(random.choices("\u0020-\u007e", k=5))


def gen_BLOCK_COMMENT_9(depth=3):
    # Generates a block comment
    return "/* Unconnected-drive-specific block comment */"

def gen_NEWLINE_7(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_6(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_UNCONNECTED_DRIVE_VALUE(depth=3):
    # Generates a unconnected drive value (pull0 or pull1) and pops the mode
    return random.choice(["pull0", "pull1"])


def gen_MACRO_IDENTIFIER(depth=3):
    # Generates a macro identifier
    return gen_identifier(depth-1)  # Assumes gen_identifier(depth-1) is implemented for ESCAPED_IDENTIFIER and SIMPLE_IDENTIFIER

def gen_NEWLINE_11(depth=3):
    # Generates a newline and pops the mode
    return "\n"

def gen_SPACE_TAB_10(depth=3):
    # Generates spaces or tabs for whitespace
    return " " * random.randint(1, 5) + "\t" * random.randint(0, 2)

def gen_ASCII_ANY(depth=3):
    # Generates any ASCII character (7-bit)
    return "".join(random.choices("\u0000-\u007f", k=5))

def gen_ASCII_NO_NEWLINE(depth=3):
    # Generates ASCII characters excluding newlines
    valid_chars = "\u0000\u0009\u000b\u000c\u000e-\u007f"
    return "".join(random.choices(valid_chars, k=5))

def gen_ASCII_NO_NEWLINE_QUOTE_BACKSLASH(depth=3):
    # Generates ASCII characters excluding newlines, quotes, and backslashes
    valid_chars = "\u0000\u0009\u000b\u000c\u000e-\u0021\u0023-\u005b\u005d-\u007f"
    return "".join(random.choices(valid_chars, k=5))

def gen_ASCII_PRINTABLE_NO_SPACE(depth=3):
    # Generates printable ASCII characters excluding spaces
    valid_chars = "\u0021-\u007e"
    return "".join(random.choices(valid_chars, k=5))

def gen_ESC_ASCII_NO_NEWLINE(depth=3):
    # Generates an escaped ASCII character excluding newlines
    return "\\" + gen_ASCII_NO_NEWLINE(depth-1)

def gen_IDENTIFIER(depth=3):
    # Generates an identifier (escaped or simple)
    if random.choice([True, False]):
        return gen_ESCAPED_IDENTIFIER(depth-1)
    else:
        return gen_SIMPLE_IDENTIFIER(depth-1)


# fragment MACRO_ARGS                         : '(' ( MACRO_ARGS | ASCII_NO_PARENTHESES)* ')';

import random

def gen_MACRO_ARGS(depth=3):
    """
    生成符合 MACRO_ARGS 产生式的字符串：
        MACRO_ARGS : '(' ( MACRO_ARGS | ASCII_NO_PARENTHESES )* ')'
    
    说明：
      - 生成的字符串以 '(' 开始，以 ')' 结束。
      - 中间部分重复 0 次或多次，每次随机选择调用 gen_MACRO_ARGS（递归调用）或 gen_ASCII_NO_PARENTHESES。
      - 为避免无限递归，使用 depth 参数控制递归深度（默认为 3）。
    """
    result = "("
    # 随机决定生成 0 到 3 个中间部分
    count = random.randint(0, 3)
    
    for _ in range(count):
        # 若还有剩余递归深度，则有 50% 机会递归调用 gen_MACRO_ARGS
        if depth > 0 and random.choice([True, False]):
            result += gen_MACRO_ARGS(depth - 1)
        else:
            result += gen_ASCII_NO_PARENTHESES(depth-1)
    
    result += ")"
    return result



# fragment NEWLINE                            : '\r'? '\n';
# fragment SPACE_TAB                          : [ \t]+;



import sys
sys.setrecursionlimit(200000)  # 将递归深度上限设置为 2000


import time
import traceback



def format_verilog_code(text):
    """
    对生成的 Verilog 代码进行简单格式化：
    - 根据关键字“module”、“function”、“task”、“begin”、“case”、“generate”、“config”等增加缩进；
    - 根据关键字“endmodule”、“endfunction”、“endtask”、“end”、“endcase”、“endgenerate”、“endconfig”等减少缩进。
    """
    lines = text.splitlines()
    indent_level = 0
    indent_size = 4
    formatted_lines = []
    # 定义增加缩进和减少缩进的关键字列表
    increase_keywords = ("module", "function", "task", "begin", "case", "generate", "config")
    decrease_keywords = ("endmodule", "endfunction", "endtask", "end", "endcase", "endgenerate", "endconfig")
    
    for line in lines:
        stripped = line.strip()
        # 如果当前行以减少缩进的关键字开头，则先减少缩进
        if stripped.startswith(decrease_keywords):
            indent_level = max(indent_level - 1, 0)
        formatted_lines.append(" " * (indent_level * indent_size) + stripped)
        # 如果当前行以增加缩进的关键字开头（并且不是单行结束语句），则增加缩进
        # 这里简单判断：如果行以其中某个关键字开头且行中不含有对应的结束关键字，则增加缩进
        if stripped.startswith(increase_keywords) and not stripped.startswith(decrease_keywords):
            indent_level += 1

    return "\n".join(formatted_lines)


if __name__ == "__main__":
    import time
    import traceback

    # 重试调用生成函数，直到成功
    while True:
        try:
            text = gen_module_declaration(4)
            # text = gen_list_of_port_declarations(4)
            # text = gen_port_implicit(4)
            # text = gen_port(4)
            # text = gen_port_explicit(4)
            # text = gen_port_declaration(4)

            break  # 成功生成则退出循环
        except Exception as e:
            print("生成过程中出错，正在重试……")
            #print(traceback.format_exc())
            time.sleep(0.1)  # 稍等后重试

    print(text)
   # # 使用 Verilog 格式化函数格式化文本
   # formatted_text = format_verilog_code(text)

   # # 将格式化后的文本写入到文件中
   # output_file = "output.v"  # 使用 .v 后缀更符合 Verilog 文件约定
   # with open(output_file, "w", encoding="utf-8") as f:
   #     f.write(formatted_text)

   # print(f"成功生成 Verilog 文本，并已写入文件：{output_file}")
