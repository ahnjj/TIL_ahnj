class HttpRequest:
    
    def __init__(self, req_msg):
        self.__parse_req_msg(req_msg)
        
    def __str__(self):
        return f'{self.__method},  {self.__url}, {self.__params}'
    
    def __parse_req_msg(self, req_msg):
        req_msg = str(req_msg, encoding='utf-8')
        req_msg_lines = self.__generate_req_msg(req_msg)
        
        req_start_line = req_msg_lines[0].split(' ')
        
        self.__method = req_start_line[0]
        url_tmp = req_start_line[1]
        
        if '?' in url_tmp:
            # ?name=hmd&age=10&color=100
            parm_str = url_tmp[url_tmp.index('?')+1:]
            parms_pairs = parm_str.split('&')
            
            params = {}
            for pair in parms_pairs:
                param_name = pair.split('=')[0]
                param_value = pair.split('=')[1]
                
                if param_name in params:
                    params[param_name] = params[param_name].append(param_value)
                else:
                    params[param_name] = [param_value]

            self.__params = params
            self.__url = url_tmp[0:url_tmp.index('?')]
        else:
            self.__url = url_tmp
        
        req_header = req_msg_lines[1:req_msg_lines.index('')]