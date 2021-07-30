from web3 import Web3
import json
import time


bsc_url = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc_url))
pancakeabi = json.loads('[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},'
                        '{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable",'
                        '"type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address",'
                        '"name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{'
                        '"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address",'
                        '"name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256",'
                        '"name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to",'
                        '"type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],'
                        '"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},'
                        '{"internalType":"uint256","name":"liquidity","type":"uint256"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",'
                        '"name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address",'
                        '"name":"to","type":"address"},{"internalType":"uint256","name":"deadline",'
                        '"type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256",'
                        '"name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH",'
                        '"type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],'
                        '"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{'
                        '"internalType":"address","name":"","type":"address"}],"stateMutability":"view",'
                        '"type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut",'
                        '"type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},'
                        '{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn",'
                        '"outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],'
                        '"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn",'
                        '"type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],'
                        '"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut",'
                        '"type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{'
                        '"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]",'
                        '"name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{'
                        '"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view",'
                        '"type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},'
                        '{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut",'
                        '"outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],'
                        '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA",'
                        '"type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],'
                        '"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],'
                        '"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address",'
                        '"name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB",'
                        '"type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256",'
                        '"name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to",'
                        '"type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],'
                        '"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",'
                        '"name":"token","type":"address"},{"internalType":"uint256","name":"liquidity",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address",'
                        '"name":"to","type":"address"},{"internalType":"uint256","name":"deadline",'
                        '"type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256",'
                        '"name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH",'
                        '"type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{'
                        '"internalType":"address","name":"token","type":"address"},{"internalType":"uint256",'
                        '"name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],'
                        '"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{'
                        '"internalType":"uint256","name":"amountETH","type":"uint256"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",'
                        '"name":"token","type":"address"},{"internalType":"uint256","name":"liquidity",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address",'
                        '"name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},'
                        '{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8",'
                        '"name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},'
                        '{"internalType":"bytes32","name":"s","type":"bytes32"}],'
                        '"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256",'
                        '"name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH",'
                        '"type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{'
                        '"internalType":"address","name":"token","type":"address"},{"internalType":"uint256",'
                        '"name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin",'
                        '"type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax",'
                        '"type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32",'
                        '"name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],'
                        '"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{'
                        '"internalType":"uint256","name":"amountETH","type":"uint256"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",'
                        '"name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB",'
                        '"type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256",'
                        '"name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to",'
                        '"type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},'
                        '{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8",'
                        '"name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},'
                        '{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit",'
                        '"outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},'
                        '{"internalType":"uint256","name":"amountB","type":"uint256"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path",'
                        '"type":"address[]"},{"internalType":"address","name":"to","type":"address"},'
                        '{"internalType":"uint256","name":"deadline","type":"uint256"}],'
                        '"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts",'
                        '"type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{'
                        '"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address['
                        ']","name":"path","type":"address[]"},{"internalType":"address","name":"to",'
                        '"type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],'
                        '"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts",'
                        '"type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{'
                        '"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address['
                        ']","name":"path","type":"address[]"},{"internalType":"address","name":"to",'
                        '"type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],'
                        '"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],'
                        '"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin",'
                        '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{'
                        '"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin",'
                        '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],'
                        '"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin",'
                        '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{'
                        '"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin",'
                        '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],'
                        '"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax",'
                        '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{'
                        '"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
                        '"name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax",'
                        '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{'
                        '"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],'
                        '"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable",'
                        '"type":"receive"}]')
erc20abi = json.loads('[{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string",'
                      '"name":"symbol","type":"string"},{"internalType":"uint256","name":"initialBalance",'
                      '"type":"uint256"},{"internalType":"address payable","name":"feeReceiver","type":"address"}],'
                      '"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{'
                      '"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,'
                      '"internalType":"address","name":"spender","type":"address"},{"indexed":false,'
                      '"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},'
                      '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner",'
                      '"type":"address"},{"indexed":true,"internalType":"address","name":"newOwner",'
                      '"type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,'
                      '"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},'
                      '{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,'
                      '"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},'
                      '{"inputs":[{"internalType":"address","name":"owner","type":"address"},'
                      '{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{'
                      '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view",'
                      '"type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},'
                      '{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{'
                      '"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable",'
                      '"type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],'
                      '"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
                      '"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{'
                      '"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},'
                      '{"inputs":[{"internalType":"address","name":"spender","type":"address"},'
                      '{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],'
                      '"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],'
                      '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"generator","outputs":[{'
                      '"internalType":"string","name":"","type":"string"}],"stateMutability":"pure",'
                      '"type":"function"},{"inputs":[],"name":"getOwner","outputs":[{"internalType":"address",'
                      '"name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{'
                      '"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256",'
                      '"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{'
                      '"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable",'
                      '"type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"",'
                      '"type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner",'
                      '"outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view",'
                      '"type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],'
                      '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{'
                      '"internalType":"string","name":"","type":"string"}],"stateMutability":"view",'
                      '"type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256",'
                      '"name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{'
                      '"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256",'
                      '"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool",'
                      '"name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{'
                      '"internalType":"address","name":"sender","type":"address"},{"internalType":"address",'
                      '"name":"recipient","type":"address"},{"internalType":"uint256","name":"amount",'
                      '"type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"",'
                      '"type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{'
                      '"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership",'
                      '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version",'
                      '"outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view",'
                      '"type":"function"}]')
pancakerouter = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
wbnb = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
walletadr = ""  #这里填写钱包地址
private_key = ""  #这里填写密钥


tokencontract = "0xa53e61578ff54f1ad70186be99332a6e20b6ffa9"  #代币合约地址
howmuchbnb: float = 0.002
tokens_sell: float = 73004
slippages: float = 20 * 0.01
gasprice: float = 5.1
gaslimit: int = 700000


def wbnb_balance():
    wbnb_blance = web3.fromWei(web3.eth.getBalance(walletadr), 'ether')
    return wbnb_blance


def checksum(contract):
    tokencontract_checksum = Web3.toChecksumAddress(contract)
    return tokencontract_checksum


erc20 = web3.eth.contract(address=checksum(tokencontract), abi=erc20abi)
pancake = web3.eth.contract(address=checksum(pancakerouter), abi=pancakeabi)

def getinfo():
    '获取指定代币总供应量'
    totalsupply_no_decimals = erc20.functions.totalSupply().call()  #获取没有精度的总供应量
    decimals = erc20.functions.decimals().call()  #获取精度
    totalsupply = float(totalsupply_no_decimals/(10**decimals))  #实际总供应量
    '获取指定代币name和symbol'
    name = erc20.functions.name().call()
    symbol = erc20.functions.symbol().call()

    #print(wbnb_balance())  #查询钱包wbnb余额
    #print(name, symbol, totalsupply, decimals)
    return [name, symbol, totalsupply, decimals]


def balance(wallet, token, humanread):
    contract = web3.eth.contract(address=checksum(token), abi=erc20abi)
    tokenblance_no_decimals = contract.functions.balanceOf(checksum(wallet)).call()
    if humanread == 1:
        decimals = contract.functions.decimals().call()  #获取精度
        tokenblance = float(tokenblance_no_decimals/(10**decimals))
        return tokenblance
    else:
        return tokenblance_no_decimals

#指定bnb能兑换多少个token
def how_many_tokens_can_buy():
    amount = float(pancake.functions.getAmountsOut(web3.toWei(howmuchbnb, 'ether'), [checksum(wbnb), checksum(tokencontract)]).call()[-1])/10**getinfo()[-1]
    return amount

#卖一个目标token的价格 单位为bnb
def sell_one_token_price():
    price = web3.fromWei(int(pancake.functions.getAmountsOut(10**getinfo()[-1], [checksum(tokencontract), checksum(wbnb)]).call()[-1]), 'ether')
    return price

#买一个目标token的价格 单位为bnb
def buy_one_token_price():
    price = web3.fromWei(int(pancake.functions.getAmountsIn(10**getinfo()[-1], [checksum(wbnb), checksum(tokencontract)]).call()[0]), 'ether')
    return price

#指定token数量能兑换多少bnb
def how_many_bnb_can_get():
    price = web3.fromWei(int(pancake.functions.getAmountsOut(balance(walletadr, tokencontract, 0), [checksum(tokencontract), checksum(wbnb)]).call()[-1]), 'ether')
    return price


def buy():
    'build交易(最少获得的代币数量，[要花费的代币地址，要买的代币地址]，钱包地址，交易限制时间 当前是10min)'
    tx_info = pancake.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(int(how_many_tokens_can_buy()*(10**getinfo()[-1])*(1-slippages)), [checksum(wbnb), checksum(tokencontract)], walletadr, int(time.time()) + 10 * 60). \
        buildTransaction(
        {
            'from': walletadr,
            'value': web3.toWei(howmuchbnb, 'ether'),
            'gas': gaslimit,
            'gasPrice': web3.toWei(gasprice, 'Gwei'),
            'nonce': web3.eth.get_transaction_count(walletadr),
        }
    )
    print('wbnb余额：', wbnb_balance(), '目标代币余额：', balance(walletadr, tokencontract, 1), time.strftime("%Y-%m-%d %H:%M:%S"))
    sign_txn = web3.eth.account.sign_transaction(tx_info, private_key=private_key)
    print('交易发送中...', time.strftime("%Y-%m-%d %H:%M:%S"))
    res = web3.eth.sendRawTransaction(sign_txn.rawTransaction).hex()
    txn_receipt = web3.eth.waitForTransactionReceipt(res)
    print('Txn:', res, time.strftime("%Y-%m-%d %H:%M:%S"))
    if txn_receipt['status'] == 1:
        print('交易完成\nwbnb余额：', wbnb_balance(), str(getinfo()[1])+'余额：', balance(walletadr, tokencontract, 1), time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print('交易失败，详情查看：', 'https://bscscan.com/tx/'+res)
    return txn_receipt


def check_approved():
    print('授权检测...')
    allowance = erc20.functions.allowance(checksum(walletadr), checksum(pancakerouter)).call()
    print('授权数量：', allowance)
    return allowance


def approve():
    if check_approved() < balance(walletadr, tokencontract, 0):
        print('代币未授权，自动授权...')
        approve_info = erc20.functions.approve(checksum(pancakerouter), int(f"0x{64 * 'f'}", 16)).buildTransaction(
            {
                'from': walletadr,
                'value': web3.toWei(0, 'ether'),
                'gas': gaslimit,
                'gasPrice': web3.toWei(gasprice, 'Gwei'),
                'nonce': web3.eth.get_transaction_count(walletadr),
            }
        )
        sign_txn = web3.eth.account.sign_transaction(approve_info, private_key=private_key)
        print('授权中...', time.strftime("%Y-%m-%d %H:%M:%S"))
        res = web3.eth.sendRawTransaction(sign_txn.rawTransaction).hex()
        txn_receipt = web3.eth.waitForTransactionReceipt(res)
        print('Txn:', res, time.strftime("%Y-%m-%d %H:%M:%S"))
        if txn_receipt['status'] == 1:
            print('授权完成', time.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            print('授权失败，详情查看：', 'https://bscscan.com/tx/'+res)
    else:
        pass


def sell():
    approve()
    '(卖出数量, 最少收到的wbnb, [要花费的代币地址，要买的代币地址], 钱包地址，交易限制时间 当前是10min)'
    tx_info = pancake.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(int(tokens_sell*10**getinfo()[-1]), int(web3.toWei(how_many_bnb_can_get(), 'ether')*(1-slippages)), [checksum(tokencontract), checksum(wbnb)], walletadr, int(time.time()) + 10 * 60). \
        buildTransaction(
        {
            'from': walletadr,
            #'value': web3.toWei(howmuchbnb, 'ether'),
            'gas': gaslimit,
            'gasPrice': web3.toWei(gasprice, 'Gwei'),
            'nonce': web3.eth.get_transaction_count(walletadr),
        }
    )
    print('wbnb余额：', wbnb_balance(), '目标代币余额：', balance(walletadr, tokencontract, 1), time.strftime("%Y-%m-%d %H:%M:%S"))
    sign_txn = web3.eth.account.sign_transaction(tx_info, private_key=private_key)
    print('交易发送中...', time.strftime("%Y-%m-%d %H:%M:%S"))
    res = web3.eth.sendRawTransaction(sign_txn.rawTransaction).hex()
    txn_receipt = web3.eth.waitForTransactionReceipt(res)
    print('Txn:', res, time.strftime("%Y-%m-%d %H:%M:%S"))
    if txn_receipt['status'] == 1:
        print('交易完成\nwbnb余额：', wbnb_balance(), str(getinfo()[1])+'余额：', balance(walletadr, tokencontract, 1), time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print('交易失败，详情查看：', 'https://bscscan.com/tx/'+res)
    return txn_receipt


def latency():
    print('start')
    t1 = time.time_ns()
    status = web3.isConnected()
    if status is True:
        t2 = time.time_ns()
        print('Connected! Latency:', (t2-t1)/1000000, 'ms')
    else:
        print('Connect fail')


