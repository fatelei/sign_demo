CREATE TABLE `user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL COMMENT '用户名',
    `password` varchar(255) NOT NULL COMMENT '用户密码',
    `role` tinyint(1) NULL DEFAULT 0 COMMENT '用户角色',
    `is_active` tinyint(1) NULL DEFAULT -1 COMMENT '账户状态',
    `register_date` int(11) unsigned NULL COMMENT '注册时间',
    `permission_id` int(11) NULL COMMENT '用户权限',
    `company_id` int(11) NULL COMMENT '用户所属公司',
    `profile_id` int(11) NULL COMMENT '用户个人信息',
    `certificate_id` int(11) NULL COMMENT '证书',
    `is_delete` tinyint(1) NULL DEFAULT 0 COMMENT '用户是否被删除',
    PRIMARY KEY (`id`),
    KEY `role` (`role`, `id`),
    KEY `is_active` (`is_active`, `id`),
    UNIQUE KEY `username` (`username`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `permission` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `permission` int(11) NOT NULL COMMENT '权限描述',
    PRIMARY KEY (`id`),
    KEY `permission` (`permission`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `userprofile` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `fullname` varchar(255) NOT NULL COMMENT '用户真实姓名',
    `email` varchar(255) NULL COMMENT '用户邮箱',
    `phone` varchar(255) NULL COMMENT '用户电话',
    `is_delete` tinyint(1) NULL DEFAULT 0 COMMENT '用户个人信息是否被删除',
    PRIMARY KEY (`id`),
    KEY `fullname` (`fullname`),
    UNIQUE KEY `email` (`email`),
    UNIQUE KEY `phone` (`phone`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `user_certificate` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `enc_cert_sn` varchar(255) NOT NULL COMMENT '加密证书序列号',
    `sign_cert_sn` varchar(255) NOT NULL COMMENT '签名证书序列号',
    `is_delete` tinyint(1) NULL DEFAULT 0 COMMENT '是否被删除',
    PRIMARY KEY (`id`),
    KEY `enc_cert_sn` (`enc_cert_sn`),
    KEY `sign_cert_sn` (`sign_cert_sn`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `company` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `etp_property` varchar(255) NOT NULL COMMENT '企业性质',
    `etp_name` varchar(255) NOT NULL COMMENT '企业名称',
    `etp_address` varchar(255) NOT NULL COMMENT '企业通信地址',
    `etp_site` varchar(255) NOT NULL COMMENT '企业网址',
    `etp_phone` int(11) NOT NULL COMMENT '企业电话',
    `etp_fax` int(11) NOT NULL COMMENT '企业传真号码',
    `org_code` varchar(255) NOT NULL COMMENT '组织机构代码',
    `bs_lic_num` varchar(255) NOT NULL COMMENT '营业执照号',
    `tax_reg_num` varchar(255) NOT NULL COMMENT '税务登记号',
    `postcode` int(11) NOT NULL COMMENT '邮政编码',
    `legal_name` varchar(255) NOT NULL COMMENT '法定代表人姓名',
    `legal_phone` varchar(255) NOT NULL COMMENT '法定代表人电话',
    PRIMARY KEY (`id`),
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `contact_template` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL COMMENT '合同模板拥有者ID',
    `tpl_name` varchar(255) NOT NULL COMMENT '合同模板名称',
    `tpl_instruction` varchar(255) NOT NULL COMMENT '合同模板说明',
    `tpl_content`text NOT NULL COMMENT '合同模板内容',
    `last_update_time` int(11) unsigned NULL COMMENT '最后更新时间',
    PRIMARY KEY (`id`),
    KEY `user_id` (`user_id`),
    KEY `tpl_name` (`tpl_name`),
    KEY `last_update_time` (`last_update_time`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `contact` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL COMMENT '起草人',
    `contact_content` blob NOT NULL COMMENT '合同内容',
    `status` tinyint(1) NOT NULL DEFAULT -1 COMMENT '签订状态',
    `sign_time` int(11) unsigned NULL COMMENT '签订日期',
    `seal_data` blob NOT NULL COMMENT '印章属性页数据',
    PRIMARY KEY (`id`),
    KEY `user_id` (`user_id`),
    KEY `sign_time` (`sign_time`),
    KEY `status` (`status`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `log` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `op_time` int(11) unsigned NOT NULL COMMENT '日志时间',
    `op_user` varchar(255) NOT NULL COMMENT '操作人',
    `op_target` varchar(255) NOT NULL COMMENT '事件对象',
    PRIMARY KEY (`id`),
    KEY `op_user` (`op_user`),
    KEY `op_time` (`op_time`),
    KEY `op_target` (`op_target`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


