from ansible.module_utils.basic import AnsibleModule

def sayHello(message):
    return "Custom Ansible Module - " + message

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str', required=True),
        ),
        supports_check_mode=True
    )

    #Retrieve message parameter the end-user gave in the ansible playbook
    msg = module.params['message']

    result = dict(
        response=sayHello(msg),
    )

    #module.exit_json(**result, changed=True) # success with change - yellow color
    module.exit_json(**result, changed=False) # success with no change - green color
    #module.fail_json(msg="Failed due to unknown error") - red color

if __name__ == '__main__':
    main()
