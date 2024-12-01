# Generated from Algoritmia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser


class AlgoritmiaVisitor(ParseTreeVisitor):

    def visitRoot(self, ctx:AlgoritmiaParser.RootContext):
        return self.visitChildren(ctx)


    def visitInss(self, ctx:AlgoritmiaParser.InssContext):
        return self.visitChildren(ctx)


    def visitIns(self, ctx:AlgoritmiaParser.InsContext):
        return self.visitChildren(ctx)


    def visitInput_(self, ctx:AlgoritmiaParser.Input_Context):
        return self.visitChildren(ctx)


    def visitOutput_(self, ctx:AlgoritmiaParser.Output_Context):
        return self.visitChildren(ctx)


    def visitCondition(self, ctx:AlgoritmiaParser.ConditionContext):
        return self.visitChildren(ctx)


    def visitWhile_(self, ctx:AlgoritmiaParser.While_Context):
        return self.visitChildren(ctx)


    def visitReprod(self, ctx:AlgoritmiaParser.ReprodContext):
        return self.visitChildren(ctx)


    def visitAgregado(self, ctx:AlgoritmiaParser.AgregadoContext):
        return self.visitChildren(ctx)


    def visitCorte(self, ctx:AlgoritmiaParser.CorteContext):
        return self.visitChildren(ctx)


    def visitProcDef(self, ctx:AlgoritmiaParser.ProcDefContext):
        return self.visitChildren(ctx)


    def visitProc(self, ctx:AlgoritmiaParser.ProcContext):
        return self.visitChildren(ctx)


    def visitAssign(self, ctx:AlgoritmiaParser.AssignContext):
        return self.visitChildren(ctx)


    def visitParamsId(self, ctx:AlgoritmiaParser.ParamsIdContext):
        return self.visitChildren(ctx)


    def visitParamsExpr(self, ctx:AlgoritmiaParser.ParamsExprContext):
        return self.visitChildren(ctx)


    def visitLista(self, ctx:AlgoritmiaParser.ListaContext):
        return self.visitChildren(ctx)


    def visitConsult(self, ctx:AlgoritmiaParser.ConsultContext):
        return self.visitChildren(ctx)


    def visitMod(self, ctx:AlgoritmiaParser.ModContext):
        return self.visitChildren(ctx)


    def visitMul(self, ctx:AlgoritmiaParser.MulContext):
        return self.visitChildren(ctx)


    def visitVar(self, ctx:AlgoritmiaParser.VarContext):
        return self.visitChildren(ctx)


    def visitParens(self, ctx:AlgoritmiaParser.ParensContext):
        return self.visitChildren(ctx)


    def visitNum(self, ctx:AlgoritmiaParser.NumContext):
        return self.visitChildren(ctx)


    def visitSz(self, ctx:AlgoritmiaParser.SzContext):
        return self.visitChildren(ctx)


    def visitLt(self, ctx:AlgoritmiaParser.LtContext):
        return self.visitChildren(ctx)


    def visitSum(self, ctx:AlgoritmiaParser.SumContext):
        return self.visitChildren(ctx)


    def visitString(self, ctx:AlgoritmiaParser.StringContext):
        return self.visitChildren(ctx)


    def visitNota(self, ctx:AlgoritmiaParser.NotaContext):
        return self.visitChildren(ctx)


    def visitLst(self, ctx:AlgoritmiaParser.LstContext):
        return self.visitChildren(ctx)


    def visitEq(self, ctx:AlgoritmiaParser.EqContext):
        return self.visitChildren(ctx)


    def visitGt(self, ctx:AlgoritmiaParser.GtContext):
        return self.visitChildren(ctx)


    def visitDiv(self, ctx:AlgoritmiaParser.DivContext):
        return self.visitChildren(ctx)


    def visitMin(self, ctx:AlgoritmiaParser.MinContext):
        return self.visitChildren(ctx)


    def visitConsul(self, ctx:AlgoritmiaParser.ConsulContext):
        return self.visitChildren(ctx)


    def visitGet(self, ctx:AlgoritmiaParser.GetContext):
        return self.visitChildren(ctx)


    def visitLet(self, ctx:AlgoritmiaParser.LetContext):
        return self.visitChildren(ctx)


    def visitNeq(self, ctx:AlgoritmiaParser.NeqContext):
        return self.visitChildren(ctx)


    def visitSiz(self, ctx:AlgoritmiaParser.SizContext):
        return self.visitChildren(ctx)



del AlgoritmiaParser